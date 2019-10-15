# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 

# This class represents a directed graph 
# using adjacency list representation 
class Graph: 

	# Constructor 
	def __init__(self): 

		# default dictionary to store graph 
		self.graph = defaultdict(list) 
		self.numberOfVertices = 0

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 
		self.numberOfVertices +=1

# Function to print a DFS of graph 
def DFS(graph, start, key): 
	if(graph is not None):
		stack = []
		print("Number of vertices",len(graph.graph))
		DFSRecursive(graph, stack, None, start, key)
	return -1

def DFSRecursive(graph, stack, visited, current, key):

	if(current >= 0 and current < len(graph.graph)):
		stack.append(current)
		print("Current:",current)
		for edge in graph.graph[current]:
			print("edge:",edge)
			DFSRecursive(graph, stack, visited, edge, key)
	return -1
	

def findLCA(graph, key1, key2):
	return -1

def main():
	graph = Graph()
	graph.addEdge(1,2)
	graph.addEdge(1,3)
	graph.addEdge(2,4)
	graph.addEdge(2,5)
	graph.addEdge(3,6)
	graph.addEdge(3,7)
	DFS(graph,1,7)

if __name__ == "__main__":
    main()