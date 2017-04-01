To run the code in the terminal:

python EschCache.py <JSON input file> <JSON file to write solution to>

My python code, "EschCache.py" implements recursive DFS search with memoization for an escape path. The caching was meant to speed up the runtime, as I realized how expensive naive backtracking could be with larger inputs. By tracking failed paths, I could ensure the code would not be repeating said recursive calls.
Although I interpreted the prompt to mean there should always be a possible escape path, my code returns an empty list if a valid escape path does not exist.

I abstracted a helper function "isSafe" that checks if a possible step is "safe" by checking if the incoming position is beyond the reach of the blast and does not hit an asteroid!
My initial wrapper function simply handles inputs and parses them into usable python objects before letting the recursive DFS helper do all the heavy lifting.

The folder also includes a few JSON files that I used to test my method before running the heroku app.

Some cases I tested included:
- No asteroids and t_per_blast_move of 0 would mean death, resulting in an empty path indicating no solution
- Any t_per_blast_move of 0 would mean death for that matter
- No asteroids and a t_per_blast_move > 0 would mean a single acceleration of 1 is needed
- Another file that yielded no solution
- A file that was around half the length of the given JSON file
- Paths where there would be more than one solution
- The comprehensive and lengthy provided JSON file

I also initially began trying to implement a BFS version that tracked different paths in order to find the optimal solution, but was running low on time. I had a lot of fun with this challenge and would love to hear about what how you would have gone about finding an optimal solution!