# Python Program for Lowest Common Ancestor in a Binary Tree 
# O(n) solution to find LCS of two given values n1 and n2 

# A binary tree node 
class Node: 
	# Constructor to create a new binary node 
	def __init__(self, key): 
		self.key = key 
		self.left = None
		self.right = None
		self.visited = False

def findLCA(root, key1, key2):

	if(root is not None):
		if(root.left is None and root.right is None and (key1 is not key2)):
			return -1
	
	return findLCARecursive(root, key1, key2, [False], [False])

def findLCARecursive(root, key1, key2, found1, found2):

	# If the node is null return
	if(root is None):
		print("root is none")
		return -1

	# If the node has been visited return as we have found a cycle
	if(root.visited is True):
		print(root.key, key1, key2, found1, found2, "cycle has occured")
		return -1

	root.visited = True
	left_subtree = findLCARecursive(root.left, key1, key2, found1, found2)
	right_subtree = findLCARecursive(root.right, key1, key2, found1, found2)

	if(root.key is key1):
		found1[0] = True
		return root.key
		
	if(root.key is key2):
		found2[0] = True
		return root.key
		
	if(found1[0] is True and found2[0] is True):
		if(left_subtree is not -1 and right_subtree is not -1):
			return root.key
		elif(left_subtree is not -1):
			return left_subtree
		else:
			return right_subtree

	if(left_subtree is not -1):
		return left_subtree
	
	if(right_subtree is not -1):
		return right_subtree
	
	return -1
