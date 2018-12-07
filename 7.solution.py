import re


class Node:
	def __init__(self, node_id):
		self.id = node_id
		self.parents = []
		self.children = []
		self.work_remaining = 60 + ord(node_id.upper()) - 64 
	def add_parent(self, p_id):
		if p_id not in self.parents:
			self.parents.append(p_id)
	def add_child(self, p_id):
		if p_id not in self.children:
			self.children.append(p_id)
	def print(self):
		print(self.id)
		print(self.work_remaining)
		print(self.parents)
		print(self.children)
	
class Step:
	def __init__(self, string):
		r = re.search(r"Step (\w) must be finished before step (\w) can begin", string)
		self.parent = r.group(1)
		self.child = r.group(2)

class WorkEngine:
	def __init__(self, nodes, worker_count):
		self.time = 0
		self.nodes = nodes
		self.available_nodes = []
		for node in nodes.values():
			if len(node.parents) == 0:
				self.available_nodes.append(node.id)
		self.workers = [None] * worker_count
		self.path = []
	def run(self):
		while len(self.available_nodes) != 0 or self.workers != [None] * len(self.workers):
			self.do_cycle()
			print(self.workers)
		print(self.time)
		print(self.path)
	def do_cycle(self):
		self.time += 1
		for i, work_id in enumerate(self.workers):
			if work_id is None:
				self.claim_next_node(i)
		for i, work_id in enumerate(self.workers):
			if work_id is not None:
				self.do_work(i, work_id)
	def do_work(self, worker_i, work_id):
		self.nodes[work_id].work_remaining -= 1
		if self.nodes[work_id].work_remaining == 0:
			self.path.append(work_id)
			for child_id in self.nodes[work_id].children:
				self.nodes[child_id].parents.remove(work_id)
				if len(self.nodes[child_id].parents) == 0:
					self.available_nodes.append(child_id)
			self.workers[worker_i] = None
	def claim_next_node(self, worker_i):
		self.available_nodes.sort()
		if len(self.available_nodes) != 0:
			self.workers[worker_i] = self.available_nodes.pop(0)


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

	e = WorkEngine(nodes, 5)
	e.run()
	exit()

