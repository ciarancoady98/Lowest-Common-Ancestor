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

	if(root == None):
		return -1

	if(root.key == key1 or root.key == key2):
		return root.key

	

	return -1

def findLCARecursive(root, key):
	if(root.key == key):
		return True
	if(root.left != None):
		return findLCARecursive(root.left, key)
	if(root.right != None):
		return findLCARecursive(root.right, key)
	return False
