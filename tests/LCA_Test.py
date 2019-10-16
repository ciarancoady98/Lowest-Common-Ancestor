import unittest
import sys
sys.path.append('../src')
import Graph

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