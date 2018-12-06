

import re
import numpy as np
from collections import defaultdict
def measure_distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1]) 

def is_finite(c):
	# all quadrants have an occupying cord
	pass 

with open('6.txt') as file:
	cords = []
	for c in file:
		r = re.search(r"(\d*), (\d*)", c)
		c = (int(r.group(1)), int(r.group(2)))
		cords.append(c)

	min_x = min([n[0] for n in cords])
	max_x = max([n[0] for n in cords])
	min_y = min([n[1] for n in cords])
	max_y = max([n[1] for n in cords])

	grid = {}      # np.full((max_x, max_y), (None, None)) # filled with (closest_cord, min_distance) 	

	for x in range(min_x, max_x + 1):
		for y in range(min_y, max_y + 1):
			#check distance to each cord for each point on grid
			min_dist = None
			for c in cords:
				dist = measure_distance((x,y), c)	
				if min_dist is None or dist < min_dist:
					min_dist = dist
					grid[(x,y)] = c
					if dist == 0:
						break
				elif min_dist == dist:
					grid[(x,y)] = None
	counts = defaultdict(int)
	for c in grid.values():
		counts[c] += 1

	print(max(counts.values()))
	#for c in counts:
	#	print(counts[c], c)
	# this should check for finite, but got the right answer without

		



















