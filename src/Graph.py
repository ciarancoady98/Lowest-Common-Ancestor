# Author Ciaran Coady
# Student Number 17326951
# Python program that takes a brute force approach
# to find the lowest common ancestor of two nodes in
# a directed acyclic graph.
# This class creates the node for a graph that stores
# a key
class Node:
	def __init__(self, key):
		self.key = key

# This class constructs an adjacency list 
# representation of a directed graph
class Graph: 
	def __init__(self, noOfVertices): 

		# Initialise the adjacency array
		# with the number of vertices
		self.graph = []
		self.noOfVertices = noOfVertices
		i = 0
		while(i <= noOfVertices):
			self.graph.append([])
			i+=1
		self.vertices = []
		self.hasEdges = False
	
	# Function to add a vertex to the graph
	def addVertex(self, key):
		self.vertices.append(key)

	# Function to add an edge to the graph 
	def addEdge(self,u,v): 
		self.graph[u.key].append(v)
		self.hasEdges = True

	# Function to print the graph
	def printGraph(self):
		print(self.graph) 

	# Returns if nodes in the graph are connected by edges
	def isConnected(self):
		return self.hasEdges

# A helper function that does a DFS of the graph in search of the keys
# and if found, returns paths to those nodes 
def LCARecursive(graph, stack, visited, current, key1, key2, paths1, paths2):
	if(current >= 0 and current <= graph.noOfVertices):
		stack.append(current)
		if(current is key1):
			paths1.append(list(stack))
		if(current is key2):
			paths2.append(list(stack))
		for node in graph.graph[current]:
			LCARecursive(graph, stack, visited, node.key, key1, key2, paths1, paths2)
		stack.pop()
	return
	

def findLCA(graph, start, key1, key2):
	if(graph is not None):
		# Check if the graph is just single nodes with no edges
		if(graph.isConnected() is True):
			# Keep track of the current path
			stack = []
			# Store paths to nodes that we find
			paths1 = []
			paths2 = []
			# Do a DFS in search of keys, if we find a key store it to its path
			LCARecursive(graph, stack, None, start, key1, key2, paths1, paths2)
			greatestCommonAncestor = -1
			depth = -1
			# Nested loops to iterate through all the paths and compare
			# to find common ancestors
			for path1 in paths1 :
				for path2 in paths2 :
					len1 = len(path1)
					len2 = len(path2)
					length = 0
					if(len1 >= len2):
						length = len1
					else:
						length = len2
					i = 0
					currentCommonAncestor = -1
					while i < length :
						path1Node = -1
						path2Node = -1
						if(i<len1):
							path1Node = path1[i]
						if(i<len2):
							path2Node = path2[i]
						if(path1Node == path2Node):
							currentCommonAncestor = path1Node
						elif(i > depth):
							greatestCommonAncestor = currentCommonAncestor
							depth = i
							break
						i += 1
			return greatestCommonAncestor
		else :
			print("key1:",key1," key2:",key2)
			# Check if both keys are the same and the key is in the graph
			if(key1 is key2):
				for vertex in graph.vertices:
					if(vertex is key1):
						return key1
			# Otherwise we know these nodes are not connected so return -1
			return -1
	else:
		return -1