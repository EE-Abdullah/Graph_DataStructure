class Graph:
	def __init__(self, nodes, is_directed=False):
		"""
		:param: nodes: list of string values of nodes e.g., A, B.
		"""
		self.nodes = nodes
		self.adj_list = {}
		self.is_directed = is_directed
		self.path = ""
		self.traversed_nodes = []
		for node in self.nodes:
			self.adj_list[node] = []	
	
	
	def add_edge(self, u, v):
		if (u == v):
			print("cannot add edge from a node to itself") 
		elif (v in self.adj_list[u]):
			print("Edge from %s to %s already exists" %(u, v))	

		else:
			self.adj_list[u].append(v)
			if not self.is_directed:
				self.adj_list[v].append(u)
	

	def neighbors(self, node):
		return self.adj_list[node]


	def print_graph(self):
		for node in self.nodes:
			print(node, "->", self.adj_list[node])
	
	def degree(self, node):
		return len(self.adj_list[node])
			
	
	def eccentricity(self, node):
		return "ToDo"


	def radius(self):
		return "ToDo"

	
	def diameter(self):
		return "ToDo"


	def is_central_point(self, node):
		return "ToDo"


	def centre(self):
		return "ToDo"


	def circumference(self):
		return "ToDo"

	
	def girth(self):
		return "ToDo"


	def is_connected(self):
		return "ToDo"


	def search(self, node_a, node_b):
		self.path = ""
		self.found = False
		self.traversed_nodes = []
		return self.recursive_search(node_a, node_b)


	def recursive_search(self, node_a, node_b):
		current_node = node_a
		self.traversed_nodes.append(current_node)
		if node_b in self.neighbors(current_node):
			self.found = True
			self.path += f"{current_node}->{node_b}"
			return self.path
		elif len(self.neighbors(current_node)) >= 2:
			for adj_node in self.neighbors(current_node):
				if adj_node in self.traversed_nodes:
					continue
				self.recursive_search(adj_node, node_b)
				if self.found:
					self.path = f"{current_node}->" + self.path
					return self.path 				



nodes = ["A", "B", "C", "D", "E", "F", "G"]
graph = Graph(nodes)
graph.add_edge("A", "B")
graph.add_edge("A", "D")
graph.add_edge("B", "C")
graph.add_edge("D", "C")
graph.add_edge("C", "F")
graph.add_edge("C", "E")
graph.add_edge("F", "G")
graph.add_edge("E", "G")
