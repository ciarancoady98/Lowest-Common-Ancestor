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

	# function to add an edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

# Function to print a BFS of graph 
def DFS(graph, start, key): 

	# Mark all the vertices as not visited 
	visited = []
	for(vertex in graph.graph):
		visited[vertex] = False

	# Create a stack for DFS 
	stack = [] 

	# Mark the source node as 
	# visited and enqueue it 
	stack.append(start) 
	visited[start] = True

	while stack: 

		# Dequeue a vertex from 
		# queue and print it 
		s = queue.pop(0) 
		print (s, " ") 

		# Get all adjacent vertices of the 
		# dequeued vertex s. If a adjacent 
		# has not been visited, then mark it 
		# visited and enqueue it 
		for i in self.graph[s]: 
			if visited[i] == False: 
				queue.append(i) 
				visited[i] = True

def DFSRecursvie(graph, stack, visited, current, key):
	# Mark the current node as visited and print it 
    visited[current] = true; 
    cout << v << " "; 
  
    // Recur for all the vertices adjacent to this vertex 
    list<int>::iterator i; 
    for(i = adj[v].begin(); i != adj[v].end(); ++i) 
        if(!visited[*i]) 
            DFSUtil(*i, visited); 
	return -1

def findLCA(graph, key1, key2):
	return -1
