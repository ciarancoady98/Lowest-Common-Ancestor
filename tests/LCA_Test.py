import unittest
import sys
sys.path.append('../src')
import LCA

class TestfindLCA(unittest.TestCase):

    def test_null_graph(self):
        #  Testing a null input
        self.assertEqual(LCA.findLCA(None, 1, 0, 0), -1, "Should be -1")
        self.assertEqual(LCA.findLCA(None, 1, 1, 5), -1, "Should be -1")
        self.assertEqual(LCA.findLCA(None, 1, -10, 6), -1, "Should be -1")

    def test_empty_graph(self):
        graph = LCA.Graph(1)
        graph.addEdge(LCA.Node(1), None)
        #  Testing with a single leaf node and keys not in the tree
        self.assertEqual(LCA.findLCA(graph, 1, 1, 1), -1, "Should be 1")
        self.assertEqual(LCA.findLCA(graph, 1, 1, 5), -1, "Should be -1")
        self.assertEqual(LCA.findLCA(graph, 1, -10, 6), -1, "Should be -1")

    def test_balanced_tree(self):
        #   Testing a simple balanced binary tree
        #
        #               1
        #       |               |
        #       2               3
        #   |       |       |       |
        #   4       5       6       7
        #
        graph = LCA.Graph(7)
        graph.addEdge(LCA.Node(1),LCA.Node(2))
        graph.addEdge(LCA.Node(1),LCA.Node(3))
        graph.addEdge(LCA.Node(2),LCA.Node(4))
        graph.addEdge(LCA.Node(2),LCA.Node(5))
        graph.addEdge(LCA.Node(3),LCA.Node(6))
        graph.addEdge(LCA.Node(3),LCA.Node(7))

        self.assertEqual(LCA.findLCA(graph, 1, 4, 5), 2, "Should be 2")
        self.assertEqual(LCA.findLCA(graph, 1, 4, 6), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(graph, 1, 3, 4), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(graph, 1, 2, 4), 2, "Should be 2")

        
        
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

        graph = LCA.Graph(7)
        graph.addEdge(LCA.Node(1),LCA.Node(2))
        graph.addEdge(LCA.Node(2),LCA.Node(3))
        graph.addEdge(LCA.Node(3),LCA.Node(4))
        graph.addEdge(LCA.Node(4),LCA.Node(5))
        graph.addEdge(LCA.Node(5),LCA.Node(6))
        graph.addEdge(LCA.Node(6),LCA.Node(7))

        self.assertEqual(LCA.findLCA(graph, 1, 4, 5), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(graph, 1, 4, 6), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(graph, 1, 3, 4), 3, "Should be 3")
        self.assertEqual(LCA.findLCA(graph, 1, 2, 4), 2, "Should be 2")

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
        graph = LCA.Graph(9)
        graph.addEdge(LCA.Node(1),LCA.Node(2))
        graph.addEdge(LCA.Node(1),LCA.Node(3))
        graph.addEdge(LCA.Node(2),LCA.Node(4))
        graph.addEdge(LCA.Node(2),LCA.Node(5))
        graph.addEdge(LCA.Node(3),LCA.Node(6))
        graph.addEdge(LCA.Node(3),LCA.Node(7))
        graph.addEdge(LCA.Node(4),LCA.Node(8))
        graph.addEdge(LCA.Node(5),LCA.Node(8))
        graph.addEdge(LCA.Node(6),LCA.Node(9))
        graph.addEdge(LCA.Node(7),LCA.Node(9))

        self.assertEqual(LCA.findLCA(graph, 1, 4, 5), 2, "Should be 2")
        self.assertEqual(LCA.findLCA(graph, 1, 4, 6), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(graph, 1, 3, 4), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(graph, 1, 2, 4), 2, "Should be 2")
        self.assertEqual(LCA.findLCA(graph, 1, 4, 8), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(graph, 1, 8, 4), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(graph, 1, 8, 5), 5, "Should be 5")
        self.assertEqual(LCA.findLCA(graph, 1, 6, 9), 6, "Should be 6")
        self.assertEqual(LCA.findLCA(graph, 1, 7, 9), 7, "Should be 7")


if __name__ == '__main__':
    unittest.main()