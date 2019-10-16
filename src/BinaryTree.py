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
