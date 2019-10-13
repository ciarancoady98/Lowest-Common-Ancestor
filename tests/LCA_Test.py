import unittest
import sys
sys.path.append('../src')
import LCA

class TestfindLCA(unittest.TestCase):

    def test_null_node(self):
        testNode = LCA.Node(None)
        self.assertEqual(testNode.key,None, "Should be null")

    def test_null_tree(self):
        ## Test 1 ##
        #  Testing a null input
        self.assertEqual(LCA.findLCA(None, 0, 0), -1, "Should be -1")
        self.assertEqual(LCA.findLCA(None, 1, 5), -1, "Should be -1")
        self.assertEqual(LCA.findLCA(None, -10, 6), -1, "Should be -1")

    def test_leaf_node(self):
        ## Test 2 ##
        #  Testing with a single leaf node and keys not in the tree
        self.assertEqual(LCA.findLCA(LCA.Node(1), 1, 1), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(LCA.Node(1), 1, 5), -1, "Should be -1")
        self.assertEqual(LCA.findLCA(LCA.Node(1), -10, 6), -1, "Should be -1")

    def test_node_with_cycle(self):
        ## Test 3 ##
        # Testing a node that has its self as its child
        root = LCA.Node(1)
        root.left = root
        root.right = root
        self.assertEqual(LCA.findLCA(root, 1, 1), 1, "Should be 1")

    def test_balanced_tree(self):
        ## Test 3 ##
        #   Testing a simple balanced binary tree
        #
        #               1
        #       |               |
        #       2               3
        #   |       |       |       |
        #   4       5       6       7
        #
        root = LCA.Node(1) 
        root.left = LCA.Node(2) 
        root.right = LCA.Node(3) 
        root.left.left = LCA.Node(4) 
        root.left.right = LCA.Node(5) 
        root.right.left = LCA.Node(6) 
        root.right.right = LCA.Node(7) 

        self.assertEqual(LCA.findLCA(root, 4, 5), 2, "Should be 2")
        self.assertEqual(LCA.findLCA(root, 4, 6), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(root, 3, 4), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(root, 2, 4), 2, "Should be 2")

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

        root = LCA.Node(1) 
        root.left = LCA.Node(2) 
        root.left.left = LCA.Node(3) 
        root.left.left.left = LCA.Node(4) 
        root.left.left.left.left = LCA.Node(5) 
        root.left.left.left.left.left = LCA.Node(6) 
        root.left.left.left.left.left.left = LCA.Node(7) 

        self.assertEqual(LCA.findLCA(root, 4, 5), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(root, 4, 6), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(root, 3, 4), 3, "Should be 3")
        self.assertEqual(LCA.findLCA(root, 2, 4), 2, "Should be 2")

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
        
        root = LCA.Node(1) 
        root.right = LCA.Node(2) 
        root.right.right = LCA.Node(3) 
        root.right.right.right = LCA.Node(4) 
        root.right.right.right.right = LCA.Node(5) 
        root.right.right.right.right.right = LCA.Node(6) 
        root.right.right.right.right.right.right = LCA.Node(7) 

        self.assertEqual(LCA.findLCA(root, 4, 5), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(root, 4, 6), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(root, 3, 4), 3, "Should be 3")
        self.assertEqual(LCA.findLCA(root, 2, 4), 2, "Should be 2")

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
        root = LCA.Node(1) 
        root.left = LCA.Node(2) 
        root.right = LCA.Node(3) 
        root.left.left = LCA.Node(4) 
        root.left.right = LCA.Node(5) 
        root.right.left = LCA.Node(6) 
        root.right.right = LCA.Node(7) 
        sharedNode1 = LCA.Node(8)
        root.left.left.right = sharedNode1
        root.left.right.left = sharedNode1
        sharedNode2 = LCA.Node(9)
        root.right.left.right = sharedNode2
        root.right.right.left = sharedNode2

        self.assertEqual(LCA.findLCA(root, 4, 5), 2, "Should be 2")
        self.assertEqual(LCA.findLCA(root, 4, 6), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(root, 3, 4), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(root, 2, 4), 2, "Should be 2")
        self.assertEqual(LCA.findLCA(root, 4, 8), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(root, 8, 4), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(root, 8, 5), 5, "Should be 5")
        self.assertEqual(LCA.findLCA(root, 6, 9), 6, "Should be 6")
        self.assertEqual(LCA.findLCA(root, 7, 9), 7, "Should be 7")


if __name__ == '__main__':
    unittest.main()