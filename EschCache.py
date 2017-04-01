import json
from sys import argv

script, myFile, myout = argv

# Wrapper function that calls DFS recursive helper
# Returns empty list if no escape route possible. Otherwise, returns list of accelerations at each pt in time starting at t=1

def chartAccel(myIn, Out):
	data = open(myIn, 'r')
	myOut = open(Out, 'w')
	JSON = json.load(data)
	blastpermov = JSON['t_per_blast_move']
	asteroidsList = JSON['asteroids']
	
	astlen = len(asteroidsList)

	# A dictionary that will be used to cache invalid paths to prevent repetition
	invalids = {}
	accelList=[]

	# To be returned if no path possible to escape death!
	outlist = []

	if asteroidsList and blastpermov > 0:
		asteroidsList.insert(0, None)
		outlist = chartAccelHelper(blastpermov, accelList, asteroidsList, 0, 0, 0, astlen, invalids)
	elif blastpermov > 0:
		outlist = [1]

	json.dump(outlist, myOut)
	data.close()
	myOut.close()

#Tests if next step will end up in death
def isSafe(t, astlen, asteroidsList, position, velocity, blastpermov):

	eschatonblast = t // blastpermov
	
	if position >= eschatonblast and position > 0:
		if position > astlen:
			return True
		else:
			poff = asteroidsList[position]['offset'] 
			ptpac = asteroidsList[position]['t_per_asteroid_cycle']
			if (position == 0 or (poff + t) % ptpac != 0):
				return True 
	return False


#Recursive DFS with caching that does heavy lifting of searching paths

def chartAccelHelper(blastpermov, accelList, asteroidsList, velocity, position, t, astlen, invalids):
		
	t+=1

	if position >= astlen:
		return accelList

	for atotry in range(1, -2, -1):
		trypos = position + velocity + atotry
		tryvel = velocity + atotry
		if trypos in invalids and tryvel in invalids[trypos]:
			continue
		if isSafe(t, astlen, asteroidsList, trypos, velocity, blastpermov):
			trylist = accelList
			trylist.insert(t-1, atotry)
			tryA = chartAccelHelper(blastpermov, trylist, asteroidsList, tryvel, trypos, t, astlen, invalids)
			if tryA:
				return tryA
		# Caching the positions to a list of velocities which fail to get them to a "safe" next position
	if trypos in invalids:
		if velocity-1 not in invalids[trypos]:
			invalids[trypos].insert(0, velocity-1)
		if velocity not in invalids[trypos]:
			invalids[trypos].insert(0, velocity)
		if velocity+1 not in invalids[trypos]:
			invalids[trypos].insert(0, velocity+1)
	else:
		invalids[trypos]=[velocity-1, velocity, velocity+1]
	return []

		
chartAccel(myFile, myout)