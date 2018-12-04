import re

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
	
	def overlaps_with(self, other_claim):
		occupied_space = {}

class Fabric:
	def __init__(self):
		self.occupied_space = set()

	def mark_claim(self, claim):
		for ix in range(claim.x, claim.x + claim.w):
			for iy in range(claim.y, claim.y + claim.h):
				self.mark_space_occupied(ix, iy)
		print(self.occupied_space)

	def mark_space_occupied(self, x, y):
		self.occupied_space.add(self.hash_loc(x,y))
	
	def hash_loc(self, x, y):
		return str(x) + ':' + str(y)

with open('3.txt') as file:
	for line in file:
		claim = Claim(line.strip())
		claim.print()
		fab = Fabric()
		fab.mark_claim(claim)
		exit()
