# Author Ciaran Coady
# Python program that takes a brute force approach
# to find the lowest common ancestor of two nodes in
# a directed acyclic graph.
from collections import defaultdict 

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

	# Function to add an edge to the graph 
	def addEdge(self,u,v): 
		self.graph[u.key].append(v)

	# Function to print the graph
	def printGraph(self):
		print(self.graph) 

# A helper function that does a DFS of the graph in search of the keys
# and if found, returns paths to those nodes 
def LCARecursive(graph, stack, visited, current, key1, key2, paths1, paths2):
	if(current >= 0 and current <= graph.noOfVertices):
		stack.append(current)
		if(current is key1):
			print("Return path for key 1")
			paths1.append(list(stack))
		if(current is key2):
			print("Return path for key 2")
			paths2.append(list(stack))
		print ("start of dfs recursive : stack : ",stack," current : ",current," noOfVertices : ",graph.noOfVertices)
		for node in graph.graph[current]:
			print("edge:",current,node.key)
			LCARecursive(graph, stack, visited, node.key, key1, key2, paths1, paths2)
		stack.pop()
	return
	

def findLCA(graph, start, key1, key2):
	if(graph is not None):

		if(graph.noOfVertices > 2):
			stack = []
			paths1 = []
			paths2 = []
			LCARecursive(graph, stack, None, start, key1, key2, paths1, paths2)
			print("paths1 : ",paths1)
			print("paths2 : ",paths2)
			greatestCommonAncestor = -1
			depth = -1
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
							print("currentCommonAncestor: ", currentCommonAncestor)
						elif(i > depth):
							greatestCommonAncestor = currentCommonAncestor
							depth = i
							print("greatestCommonAncestor : ", greatestCommonAncestor)
							break
						i += 1
			print("The greatest common ancestor is : ", greatestCommonAncestor)
			return greatestCommonAncestor
		else:
			print("this graph has less than 1 vertex")
			if(key1 is graph.graph[1] or key2 is graph.graph[1]):
				return 1

	else:
		return -1