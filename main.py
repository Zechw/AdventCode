import re


class Node:
	def __init__(self, node_id):
		self.id = node_id
		self.parents = []
		self.children = []
	def add_parent(self, p_id):
		if p_id not in self.parents:
			self.parents.append(p_id)
	def add_child(self, p_id):
		if p_id not in self.children:
			self.children.append(p_id)

class Step:
	def __init__(self, string):
		r = re.search(r"Step (\w) must be finished before step (\w) can begin", string)
		self.parent = r.group(1)
		self.child = r.group(2)



with open('7.txt') as file:
	#apply steps
	steps = []
	nodes = {}
	for s in file:
		step = Step(s.strip())
		if step.parent not in nodes:
			nodes[step.parent] = Node(step.parent)
		nodes[step.parent].add_child(step.child)
		if step.child not in nodes:
			nodes[step.child] = Node(step.child)
		nodes[step.child].add_parent(step.parent)
	
	#process_steps
	available_nodes = []
	for node in nodes.values():
		if len(node.parents) == 0:
			available_nodes.append(node.id)
	
	path = []
	while len(available_nodes) != 0:
		available_nodes.sort()
		node_id = available_nodes.pop(0)
		path.append(node_id)
		for child_id in nodes[node_id].children:
			nodes[child_id].parents.remove(node_id)
			if len(nodes[child_id].parents) == 0:
				available_nodes.append(child_id)
print(path)

