# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class Graph: 

	# Constructor 
	def __init__(self, noOfVertices): 

		# Initialise the adjacency array
		self.graph = []
		self.noOfVertices = noOfVertices
		i = 0
		while(i <= noOfVertices):
			self.graph.append([])
			i+=1

	# Function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v)

	# Function to print the graph
	def printGraph(self):
		print(self.graph) 

def findLongest(list1, list2):
	if(len(list1) >= len(list2)):
		return len(list1)
	return len(list2)
	

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
		for edge in graph.graph[current]:
			print("edge:",current,edge)
			LCARecursive(graph, stack, visited, edge, key1, key2, paths1, paths2)
		stack.pop()
	return -1
	

def findLCA(graph, start, key1, key2):
	if(graph is not None):
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
						print("greatestCommonAncestor : ", greatestCommonAncestor)
					i += 1
	print("The greatest common ancestor is : ", greatestCommonAncestor)
	return greatestCommonAncestor

def main():
	graph = Graph(8)
	graph.addEdge(1,2)
	graph.addEdge(1,3)
	graph.addEdge(2,4)
	graph.addEdge(2,5)
	graph.addEdge(3,6)
	graph.addEdge(3,7)
	graph.addEdge(4,8)
	graph.addEdge(5,8)
	graph.printGraph()
	findLCA(graph,1,5,8)

if __name__ == "__main__":
    main()