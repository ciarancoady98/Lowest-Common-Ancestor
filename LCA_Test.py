import unittest
import LCA

class TestfindLCA(unittest.TestCase):

    def test_findLCA(self):
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

if __name__ == '__main__':
    unittest.main()