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
	
	# If the node is null return
	if(root is None):
		print("root is none")
		return -1

	# If the node has been visited return as we have found a cycle
	if(root.visited is True):
		print(root.key, key1, key2, "cycle has occured")
		return -1

	#root.visited = True
	left_subtree = findLCA(root.left, key1, key2)
	right_subtree = findLCA(root.right, key1, key2)

	if(root.key is key1 or root.key is key2):
		if(left_subtree is not -1):
			print(root.key, key1, key2, "root.key matches key 1 or 2 and other key in left subtree")
			return root.key
		elif(right_subtree is not -1):
			print(root.key, key1, key2, "root.key matches key 1 or 2 and other key in right subtree")
			return root.key
		else:
			print("we found a lone key")
			return root.key
	
	if(left_subtree is not -1 and right_subtree is not -1):
		print(root.key, key1, key2, "key in both subtrees")
		return root.key

	if(left_subtree is not -1):
		print(root.key, key1, key2, "key in left subtree")
		return left_subtree
	
	if(right_subtree is not -1):
		print(root.key, key1, key2, "key in right subtree")
		return right_subtree

	return -1
