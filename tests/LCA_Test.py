import unittest
import sys
sys.path.append('../src')
import BinaryTree
import Graph

class TestfindLCA_BinaryTree(unittest.TestCase):

    def test_null_node_BT(self):
        testNode = BinaryTree.Node(None)
        self.assertEqual(testNode.key,None, "Should be null")

    def test_null_tree_BT(self):
        #  Testing a null input
        self.assertEqual(BinaryTree.findLCA(None, 0, 0), -1, "Should be -1")
        self.assertEqual(BinaryTree.findLCA(None, 1, 5), -1, "Should be -1")
        self.assertEqual(BinaryTree.findLCA(None, -10, 6), -1, "Should be -1")
        
        self.assertEqual(BinaryTree.findLCA2(None, 0, 0), -1, "Should be -1")
        self.assertEqual(BinaryTree.findLCA2(None, 1, 5), -1, "Should be -1")
        self.assertEqual(BinaryTree.findLCA2(None, -10, 6), -1, "Should be -1")

    def test_leaf_node_BT(self):
        #  Testing with a single leaf node and keys not in the tree
        self.assertEqual(BinaryTree.findLCA(BinaryTree.Node(1), 1, 1), 1, "Should be 1")
        self.assertEqual(BinaryTree.findLCA(BinaryTree.Node(1), 1, 5), -1, "Should be -1")
        self.assertEqual(BinaryTree.findLCA(BinaryTree.Node(1), -10, 6), -1, "Should be -1")

        self.assertEqual(BinaryTree.findLCA2(BinaryTree.Node(1), 1, 1), 1, "Should be 1")
        self.assertEqual(BinaryTree.findLCA2(BinaryTree.Node(1), 1, 5), -1, "Should be -1")
        self.assertEqual(BinaryTree.findLCA2(BinaryTree.Node(1), -10, 6), -1, "Should be -1")

        

    def test_node_with_cycle_BT(self):
        # Testing a node that has its self as its child
        root = BinaryTree.Node(1)
        root.left = root
        root.right = root
        self.assertEqual(BinaryTree.findLCA(root, 1, 1), 1, "Should be 1")
        self.assertEqual(BinaryTree.findLCA2(root, 1, 1), 1, "Should be 1")

    def test_balanced_tree_BT(self):
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

        self.assertEqual(BinaryTree.findLCA2(root, 4, 5), 2, "Should be 2")
        self.assertEqual(BinaryTree.findLCA2(root, 4, 6), 1, "Should be 1")
        self.assertEqual(BinaryTree.findLCA2(root, 3, 4), 1, "Should be 1")
        self.assertEqual(BinaryTree.findLCA2(root, 2, 4), 2, "Should be 2")

        
        
    def test_left_leaning_tree_BT(self):
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

        self.assertEqual(BinaryTree.findLCA2(root, 4, 5), 4, "Should be 4")
        self.assertEqual(BinaryTree.findLCA2(root, 4, 6), 4, "Should be 4")
        self.assertEqual(BinaryTree.findLCA2(root, 3, 4), 3, "Should be 3")
        self.assertEqual(BinaryTree.findLCA2(root, 2, 4), 2, "Should be 2")
        

    def test_right_leaning_tree_BT(self):
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

        self.assertEqual(BinaryTree.findLCA2(root, 4, 5), 4, "Should be 4")
        self.assertEqual(BinaryTree.findLCA2(root, 4, 6), 4, "Should be 4")
        self.assertEqual(BinaryTree.findLCA2(root, 3, 4), 3, "Should be 3")


    def test_balanced_tree_common_parent_BT(self):
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

        self.assertEqual(BinaryTree.findLCA2(root, 4, 5), 2, "Should be 2")
        self.assertEqual(BinaryTree.findLCA2(root, 4, 6), 1, "Should be 1")
        self.assertEqual(BinaryTree.findLCA2(root, 3, 4), 1, "Should be 1")
        self.assertEqual(BinaryTree.findLCA2(root, 2, 4), 2, "Should be 2")
        self.assertEqual(BinaryTree.findLCA2(root, 4, 8), 4, "Should be 4")
        self.assertEqual(BinaryTree.findLCA2(root, 8, 4), 4, "Should be 4")
        self.assertEqual(BinaryTree.findLCA2(root, 8, 5), 5, "Should be 5")
        self.assertEqual(BinaryTree.findLCA2(root, 6, 9), 6, "Should be 6")
        self.assertEqual(BinaryTree.findLCA2(root, 7, 9), 7, "Should be 7")

class TestfindLCA_DAG(unittest.TestCase):

    def test_null_graph(self):
        #  Testing a null input
        self.assertEqual(Graph.findLCA(None, 1, 0, 0), -1, "Should be -1")
        self.assertEqual(Graph.findLCA(None, 1, 1, 5), -1, "Should be -1")
        self.assertEqual(Graph.findLCA(None, 1, -10, 6), -1, "Should be -1")

    def test_empty_graph(self):
        # Testing with a single leaf node and keys not in the tree
        graph = Graph.Graph(1)
        graph.addVertex(1)
        self.assertEqual(Graph.findLCA(graph, 1, 1, 1), 1, "Should be 1")
        self.assertEqual(Graph.findLCA(graph, 1, 1, 5), -1, "Should be -1")
        self.assertEqual(Graph.findLCA(graph, 1, -10, 6), -1, "Should be -1")

    def test_print_graph(self):
        graph = Graph.Graph(3)
        graph.addVertex(1)
        graph.addVertex(2)
        graph.addVertex(3)
        graph.addEdge(Graph.Node(1),Graph.Node(2))
        graph.addEdge(Graph.Node(1),Graph.Node(3))
        graph.printGraph()

    def test_balanced_tree(self):
        #   Testing a simple balanced binary tree
        #
        #               1
        #       |               |
        #       2               3
        #   |       |       |       |
        #   4       5       6       7
        #
        graph = Graph.Graph(7)
        graph.addVertex(1)
        graph.addVertex(2)
        graph.addVertex(3)
        graph.addVertex(4)
        graph.addVertex(5)
        graph.addVertex(6)
        graph.addVertex(7)
        graph.addEdge(Graph.Node(1),Graph.Node(2))
        graph.addEdge(Graph.Node(1),Graph.Node(3))
        graph.addEdge(Graph.Node(2),Graph.Node(4))
        graph.addEdge(Graph.Node(2),Graph.Node(5))
        graph.addEdge(Graph.Node(3),Graph.Node(6))
        graph.addEdge(Graph.Node(3),Graph.Node(7))

        self.assertEqual(Graph.findLCA(graph, 1, 4, 5), 2, "Should be 2")
        self.assertEqual(Graph.findLCA(graph, 1, 4, 6), 1, "Should be 1")
        self.assertEqual(Graph.findLCA(graph, 1, 3, 4), 1, "Should be 1")
        self.assertEqual(Graph.findLCA(graph, 1, 2, 4), 2, "Should be 2")
        self.assertEqual(Graph.findLCA(graph, 1, 2, 8), -1, "Should be -1")

        
        
    def test_single_path_graph(self):
        #   Testing a single path graph
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

        graph = Graph.Graph(7)
        graph.addVertex(1)
        graph.addVertex(2)
        graph.addVertex(3)
        graph.addVertex(4)
        graph.addVertex(5)
        graph.addVertex(6)
        graph.addVertex(7)
        graph.addEdge(Graph.Node(1),Graph.Node(2))
        graph.addEdge(Graph.Node(2),Graph.Node(3))
        graph.addEdge(Graph.Node(3),Graph.Node(4))
        graph.addEdge(Graph.Node(4),Graph.Node(5))
        graph.addEdge(Graph.Node(5),Graph.Node(6))
        graph.addEdge(Graph.Node(6),Graph.Node(7))

        self.assertEqual(Graph.findLCA(graph, 1, 4, 5), 4, "Should be 4")
        self.assertEqual(Graph.findLCA(graph, 1, 4, 6), 4, "Should be 4")
        self.assertEqual(Graph.findLCA(graph, 1, 3, 4), 3, "Should be 3")
        self.assertEqual(Graph.findLCA(graph, 1, 2, 4), 2, "Should be 2")

    def test_balanced_tree_common_parent(self):
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
        graph = Graph.Graph(9)
        graph.addVertex(1)
        graph.addVertex(2)
        graph.addVertex(3)
        graph.addVertex(4)
        graph.addVertex(5)
        graph.addVertex(6)
        graph.addVertex(7)
        graph.addVertex(8)
        graph.addVertex(9)
        graph.addEdge(Graph.Node(1),Graph.Node(2))
        graph.addEdge(Graph.Node(1),Graph.Node(3))
        graph.addEdge(Graph.Node(2),Graph.Node(4))
        graph.addEdge(Graph.Node(2),Graph.Node(5))
        graph.addEdge(Graph.Node(3),Graph.Node(6))
        graph.addEdge(Graph.Node(3),Graph.Node(7))
        graph.addEdge(Graph.Node(4),Graph.Node(8))
        graph.addEdge(Graph.Node(5),Graph.Node(8))
        graph.addEdge(Graph.Node(6),Graph.Node(9))
        graph.addEdge(Graph.Node(7),Graph.Node(9))

        self.assertEqual(Graph.findLCA(graph, 1, 4, 5), 2, "Should be 2")
        self.assertEqual(Graph.findLCA(graph, 1, 4, 6), 1, "Should be 1")
        self.assertEqual(Graph.findLCA(graph, 1, 3, 4), 1, "Should be 1")
        self.assertEqual(Graph.findLCA(graph, 1, 2, 4), 2, "Should be 2")
        self.assertEqual(Graph.findLCA(graph, 1, 4, 8), 4, "Should be 4")
        self.assertEqual(Graph.findLCA(graph, 1, 8, 4), 4, "Should be 4")
        self.assertEqual(Graph.findLCA(graph, 1, 8, 5), 5, "Should be 5")
        self.assertEqual(Graph.findLCA(graph, 1, 6, 9), 6, "Should be 6")
        self.assertEqual(Graph.findLCA(graph, 1, 7, 9), 7, "Should be 7")


if __name__ == '__main__':
    unittest.main()