#Author Ciaran Coady
# Python Program for Lowest Common Ancestor in a Directed Acyclic Graph

# A Node in the graph 
class Node: 
	# Constructor to create a new binary node 
	def __init__(self, key): 
		self.key = key 
		self.left = None
		self.right = None
		self.visited = False

def findLCA(root, key1, key2):
	# Check if the initial root node is null, if so don't recurse
	if(root is not None):
		if(root.left is None and root.right is None and (key1 is not key2)):
			return -1
	return findLCARecursive(root, key1, key2, [False], [False])

def findLCARecursive(root, key1, key2, found1, found2):

	# If the node is null return
	if(root is None):
		return -1

	# If the node has been visited return as we have found a cycle
	if(root.visited is True):
		return -1

	# Otherwise visit this node and search its left and right subtrees
	#root.visited = True
	left_subtree = findLCARecursive(root.left, key1, key2, found1, found2)
	right_subtree = findLCARecursive(root.right, key1, key2, found1, found2)
	# After we've made the recursive call we are no longer checking for cycles
	# so leave the node the way we found it 
	#root.visited = False

	# If we find a key, set its boolean and return the key
	if(root.key is key1):
		found1[0] = True
		return root.key
		
	if(root.key is key2):
		found2[0] = True
		return root.key

	# If we have found both keys do a case analysis to return the correct value	
	if(found1[0] is True and found2[0] is True):
		if(left_subtree is not -1 and right_subtree is not -1):
			return root.key
		elif(left_subtree is not -1):
			return left_subtree
		else:
			return right_subtree

	# If execution has fallen through to here it means the keys lie in the same
	# subtree, return the LCA
	if(left_subtree is not -1):
		return left_subtree
	
	if(right_subtree is not -1):
		return right_subtree
	
	# No keys found return failure
	return -1

##### A second implementation of finding LCA for a binary tree
##### which is sourced from geeks4geeks

# Finds the path from root node to given root of the tree. 
# Stores the path in a list path[], returns true if path 
# exists otherwise false 
def findPath( root, path, k): 

	# Baes Case 
	if root is None: 
		return False

	# Store this node is path vector. The node will be 
	# removed if not in path from root to k 
	path.append(root.key) 

	# See if the k is same as root's key 
	if root.key == k : 
		return True

	# Check if k is found in left or right sub-tree 
	if ((root.left != None and findPath(root.left, path, k)) or
			(root.right!= None and findPath(root.right, path, k))): 
		return True

	# If not present in subtree rooted with root, remove 
	# root from path and return False 
	
	path.pop() 
	return False

# Returns LCA if node n1 , n2 are present in the given 
# binary tre otherwise return -1 
def findLCA2(root, n1, n2): 

	# To store paths to n1 and n2 fromthe root 
	path1 = [] 
	path2 = [] 

	# Find paths from root to n1 and root to n2. 
	# If either n1 or n2 is not present , return -1 
	if (not findPath(root, path1, n1) or not findPath(root, path2, n2)): 
		return -1

	# Compare the paths to get the first different value 
	i = 0
	while(i < len(path1) and i < len(path2)): 
		if path1[i] != path2[i]: 
			break
		i += 1
	return path1[i-1] 
