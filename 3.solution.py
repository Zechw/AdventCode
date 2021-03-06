import re
from collections import defaultdict

class Claim:
	def __init__(self, raw):
		self.raw = raw
		r = re.search(r"#(\d*) @ (\d*),(\d*): (\d*)x(\d*)", raw)
		# print(r.groups())
		self.id = int(r.group(1))
		self.x = int(r.group(2))
		self.y = int(r.group(3))
		self.w = int(r.group(4))
		self.h = int(r.group(5))

	def print(self):
		print(self.raw)	
	
class Fabric:
	def __init__(self):
		self.occupied_space = defaultdict(int)

	def mark_claim(self, claim):
		for ix in range(claim.x, claim.x + claim.w):
			for iy in range(claim.y, claim.y + claim.h):
				self.mark_space_occupied(ix, iy)

	def mark_space_occupied(self, x, y):
		self.occupied_space[self.hash_loc(x,y)] += 1

	def get_claim_count(self, x, y):
		return self.occupied_space[self.hash_loc(x,y)]

	def hash_loc(self, x, y):
		return str(x) + ':' + str(y)

	def print(self):
		print(self.occupied_space)







sample = ['#1 @ 1,3: 4x4',
	'#2 @ 3,1: 4x4',
	'#3 @ 5,5: 2x2']

def is_not_conflicted(claim, fabric):
	for ix in range(claim.x, claim.x + claim.w):
		for iy in range(claim.y, claim.y + claim.h):
			if fabric.get_claim_count(ix, iy) > 1:
				return False
	return True			

with open('3.txt') as file:
	lines = file.readlines()
	claims = [Claim(x.strip()) for x in lines]
	fabric = Fabric()
	
	for claim in claims:
		# claim.print() 
		fabric.mark_claim(claim)
		# fabric.print()
	
	for claim in claims: # check if they have any conflicted spaces (more than 1 occupant)
		if is_not_conflicted(claim, fabric):
			print('Found it!')
			claim.print()	
	
''' part 1
	count = 0 
	for space, claims in fabric.occupied_space.items():
		if claims > 1:
			count += 1
	print(count)
'''


