class Node():
	def __init__(self):
		self.children = []
		self.metadata = []
	def print(self, offset = ''):
		print(offset + '-')
		print(offset + str(self.metadata))
		print('Child count: '+ str(len(self.children)))
		for c in self.children:
			c.print(offset + ' ')

def unpack_nodes(l):
	child_count = l.pop(0)
	metadata_count = l.pop(0)
	node = Node()
	for i in range(0, child_count):
		child, l = unpack_nodes(l)
		node.children.append(child)
	for i in range(0, metadata_count):
		node.metadata.append(l.pop(0))
	return (node, l)

def count_metadata(node):
	total = 0
	if len(node.children) > 0:
		for m in node.metadata:
			if m <= len(node.children) and m > 0:
				total += count_metadata(node.children[m-1])
	else:
		total += sum(node.metadata)
	return total

with open('8.txt') as file:
	lines = file.read()
	#lines = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
	l = [int(x) for x in lines.strip().split(' ')]
	node, remaining_l = unpack_nodes(l)
	# node.print()
	print(count_metadata(node))
