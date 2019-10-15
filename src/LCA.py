# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class Graph: 

	# Constructor 
	def __init__(self, noOfVertices): 

		# default dictionary to store graph 
		self.graph = []
		self.noOfVertices = noOfVertices
		for i in range(0,noOfVertices,1):
			self.graph.append([])
		print(self.graph)


	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

# Function to print a DFS of graph 
def DFS(graph, start, key): 
	if(graph is not None):
		stack = []
		print("Number of vertices",len(graph.graph))
		DFSRecursive(graph, stack, None, start, key)
	return -1

def DFSRecursive(graph, stack, visited, current, key):
	print ("start of dfs recursive : stack : ",stack," current : ",current," noOfVertices : ",graph.noOfVertices)
	if(current >= 0 and current < graph.noOfVertices):
		stack.append(current)
		print("Current:",current)
		for edge in graph.graph[current]:
			print("edge:",edge)
			DFSRecursive(graph, stack, visited, edge, key)
		stack.pop()
	return -1
	

def findLCA(graph, key1, key2):
	return -1

def main():
	graph = Graph(7)
	graph.addEdge(1,2)
	graph.addEdge(1,3)
	graph.addEdge(2,4)
	graph.addEdge(2,5)
	graph.addEdge(3,6)
	graph.addEdge(3,7)
	print(graph.graph)
	DFS(graph,1,7)

if __name__ == "__main__":
    main()