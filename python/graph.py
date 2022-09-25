"""
Problem: Given a list of edges, find the shortest path between two nodes.
The edges are represented as a list of tuples, where each tuple is of the form (node1, node2).
"""
class Graph:
	def __init__(self, edges):
		self.edges = edges
		self.vertices = {}
		for start, end in self.edges:
			if start in self.vertices:
				self.vertices[start].append(end)
			else:
				self.vertices[start] = [end]
	def get_paths(self, start, end, path=[]):
		path = path + [start]
		if start not in self.vertices:
			return
		if start == end:
			return [path]
		paths = []
		for node in self.vertices[start]:
			if node in path: continue
			new_paths = self.get_paths(node, end, path)
			for p in new_paths:
				paths.append(p)
		return paths
	def get_shortest_path(self, start, end, path=[]):
		path = path + [start]
		if start not in self.vertices:
			return
		if start == end:
			return [path]
		shortest_path = []
		for node in self.vertices[start]:
			if node in path: continue
			new_paths = self.get_paths(node, end, path)
			if not shortest_path or len(new_paths) < len(shortest_path):
				shortest_path = new_paths
			
		return shortest_path


edges = [
  ("Mumbai", "Paris"),
  ("Mumbai", "Dubai"),
  ("Paris", "Dubai"),
  ("Paris", "New York"),
  ("Dubai", "New York"),
  ("New York", "Toronto"),
]

start = "Mumbai"
end = "New York"

graph = Graph(edges)
print(f"All paths between: {start} and {end}: ",graph.get_paths(start,end))

print(f"Shortest path between {start} and {end}: ", graph.get_shortest_path(start,end))
