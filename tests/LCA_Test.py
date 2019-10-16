import unittest
import sys
sys.path.append('../src')
import BinaryTree

class TestfindBinaryTreeBinaryTree(unittest.TestCase):

    def test_null_node(self):
        testNode = BinaryTree.Node(None)
        self.assertEqual(testNode.key,None, "Should be null")

    def test_null_tree(self):
        #  Testing a null input
        self.assertEqual(BinaryTree.findLCA(None, 0, 0), -1, "Should be -1")
        self.assertEqual(BinaryTree.findLCA(None, 1, 5), -1, "Should be -1")
        self.assertEqual(BinaryTree.findLCA(None, -10, 6), -1, "Should be -1")

    def test_leaf_node(self):
        #  Testing with a single leaf node and keys not in the tree
        self.assertEqual(BinaryTree.findLCA(BinaryTree.Node(1), 1, 1), 1, "Should be 1")
        self.assertEqual(BinaryTree.findLCA(BinaryTree.Node(1), 1, 5), -1, "Should be -1")
        self.assertEqual(BinaryTree.findLCA(BinaryTree.Node(1), -10, 6), -1, "Should be -1")

    def test_node_with_cycle(self):
        # Testing a node that has its self as its child
        root = BinaryTree.Node(1)
        root.left = root
        root.right = root
        self.assertEqual(BinaryTree.findLCA(root, 1, 1), 1, "Should be 1")

    def test_balanced_tree(self):
        #   Testing a simple balanced binary tree
        #
        #               1
        #       |               |
        #       2               3
        #   |       |       |       |
        #   4       5       6       7
        #
        root = BinaryTree.Node(1) 
        root.left = BinaryTree.Node(2) 
        root.right = BinaryTree.Node(3) 
        root.left.left = BinaryTree.Node(4) 
        root.left.right = BinaryTree.Node(5) 
        root.right.left = BinaryTree.Node(6) 
        root.right.right = BinaryTree.Node(7) 

        self.assertEqual(BinaryTree.findLCA(root, 4, 5), 2, "Should be 2")
        self.assertEqual(BinaryTree.findLCA(root, 4, 6), 1, "Should be 1")
        self.assertEqual(BinaryTree.findLCA(root, 3, 4), 1, "Should be 1")
        self.assertEqual(BinaryTree.findLCA(root, 2, 4), 2, "Should be 2")

        
        
    def test_left_leaning_tree(self):
         ## Test 4 ##
        #   Testing a left leaning tree
        #
        #                                               1
        #                                           /
        #                                       2
        #                                   /
        #                               3
        #                           /
        #                       4
        #                   /
        #               5
        #           /
        #       6
        #   /
        # 7
        #

        root = BinaryTree.Node(1) 
        root.left = BinaryTree.Node(2) 
        root.left.left = BinaryTree.Node(3) 
        root.left.left.left = BinaryTree.Node(4) 
        root.left.left.left.left = BinaryTree.Node(5) 
        root.left.left.left.left.left = BinaryTree.Node(6) 
        root.left.left.left.left.left.left = BinaryTree.Node(7) 

        self.assertEqual(BinaryTree.findLCA(root, 4, 5), 4, "Should be 4")
        self.assertEqual(BinaryTree.findLCA(root, 4, 6), 4, "Should be 4")
        self.assertEqual(BinaryTree.findLCA(root, 3, 4), 3, "Should be 3")
        self.assertEqual(BinaryTree.findLCA(root, 2, 4), 2, "Should be 2")
        

    def test_right_leaning_tree(self):
        ## Test 5 ##
        #   Testing a right leaning tree
        #
        #   1
        #       \
        #           2
        #               \
        #                   3
        #                       \
        #                           4
        #                               \
        #                                   5
        #                                       \
        #                                           6
        #                                               \
        #                                                   7
        #
        
        root = BinaryTree.Node(1) 
        root.right = BinaryTree.Node(2) 
        root.right.right = BinaryTree.Node(3) 
        root.right.right.right = BinaryTree.Node(4) 
        root.right.right.right.right = BinaryTree.Node(5) 
        root.right.right.right.right.right = BinaryTree.Node(6) 
        root.right.right.right.right.right.right = BinaryTree.Node(7) 

        self.assertEqual(BinaryTree.findLCA(root, 4, 5), 4, "Should be 4")
        self.assertEqual(BinaryTree.findLCA(root, 4, 6), 4, "Should be 4")
        self.assertEqual(BinaryTree.findLCA(root, 3, 4), 3, "Should be 3")

    def test_balanced_tree_common_parent(self):
        ## Test 3 ##
        #   Testing a simple balanced binary tree
        #
        #               1
        #       |               |
        #       2               3
        #   |       |       |       |
        #   4       5       6       7
        #       |               |
        #       8               9
        #
        root = BinaryTree.Node(1) 
        root.left = BinaryTree.Node(2) 
        root.right = BinaryTree.Node(3) 
        root.left.left = BinaryTree.Node(4) 
        root.left.right = BinaryTree.Node(5) 
        root.right.left = BinaryTree.Node(6) 
        root.right.right = BinaryTree.Node(7) 
        sharedNode1 = BinaryTree.Node(8)
        root.left.left.right = sharedNode1
        root.left.right.left = sharedNode1
        sharedNode2 = BinaryTree.Node(9)
        root.right.left.right = sharedNode2
        root.right.right.left = sharedNode2

        self.assertEqual(BinaryTree.findLCA(root, 4, 5), 2, "Should be 2")
        self.assertEqual(BinaryTree.findLCA(root, 4, 6), 1, "Should be 1")
        self.assertEqual(BinaryTree.findLCA(root, 3, 4), 1, "Should be 1")
        self.assertEqual(BinaryTree.findLCA(root, 2, 4), 2, "Should be 2")
        self.assertEqual(BinaryTree.findLCA(root, 4, 8), 4, "Should be 4")
        self.assertEqual(BinaryTree.findLCA(root, 8, 4), 4, "Should be 4")
        self.assertEqual(BinaryTree.findLCA(root, 8, 5), 5, "Should be 5")
        self.assertEqual(BinaryTree.findLCA(root, 6, 9), 6, "Should be 6")
        self.assertEqual(BinaryTree.findLCA(root, 7, 9), 7, "Should be 7")


if __name__ == '__main__':
    unittest.main()