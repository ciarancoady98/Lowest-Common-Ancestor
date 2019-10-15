import unittest
import sys
sys.path.append('../src')
import LCA

class TestfindLCA(unittest.TestCase):
    
    # Driver code 

    # Create a graph given in 
    # the above diagram 
    g = LCA.Graph() 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
    g.BFS(2) 

    def test_null_graph(self):
        #  Testing a null input
        self.assertEqual(LCA.findLCA(None, 0, 0), -1, "Should be -1")
        self.assertEqual(LCA.findLCA(None, 1, 5), -1, "Should be -1")
        self.assertEqual(LCA.findLCA(None, -10, 6), -1, "Should be -1")

    def test_empty_graph(self):
        graph = LCA.Graph()
        #  Testing with a single leaf node and keys not in the tree
        self.assertEqual(LCA.findLCA(graph, 1, 1), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(graph, 1, 5), -1, "Should be -1")
        self.assertEqual(LCA.findLCA(graph, -10, 6), -1, "Should be -1")
    '''
    def test_node_with_cycle(self):
        # Testing a node that has its self as its child
        root = LCA.Node(1)
        root.left = root
        root.right = root
        self.assertEqual(LCA.findLCA(root, 1, 1), 1, "Should be 1")
    '''
    def test_balanced_tree(self):
        #   Testing a simple balanced binary tree
        #
        #               1
        #       |               |
        #       2               3
        #   |       |       |       |
        #   4       5       6       7
        #
        graph = LCA.Graph()
        graph.addEdge(1,2)
        graph.addEdge(1,3)
        graph.addEdge(2,4)
        graph.addEdge(2,5)
        graph.addEdge(3,6)
        graph.addEdge(3,7)

        self.assertEqual(LCA.findLCA(graph, 4, 5), 2, "Should be 2")
        self.assertEqual(LCA.findLCA(graph, 4, 6), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(graph, 3, 4), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(graph, 2, 4), 2, "Should be 2")

        
        
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

        graph = LCA.Graph()
        graph.addEdge(1,2)
        graph.addEdge(2,3)
        graph.addEdge(3,4)
        graph.addEdge(4,5)
        graph.addEdge(5,6)
        graph.addEdge(6,7)

        self.assertEqual(LCA.findLCA(graph, 4, 5), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(graph, 4, 6), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(graph, 3, 4), 3, "Should be 3")
        self.assertEqual(LCA.findLCA(graph, 2, 4), 2, "Should be 2")

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
        graph = LCA.Graph()
        graph.addEdge(1,2)
        graph.addEdge(1,3)
        graph.addEdge(2,4)
        graph.addEdge(2,5)
        graph.addEdge(3,6)
        graph.addEdge(3,7)
        graph.addEdge(4,8)
        graph.addEdge(5,8)
        graph.addEdge(6,9)
        graph.addEdge(7,9)

        self.assertEqual(LCA.findLCA(graph, 4, 5), 2, "Should be 2")
        self.assertEqual(LCA.findLCA(graph, 4, 6), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(graph, 3, 4), 1, "Should be 1")
        self.assertEqual(LCA.findLCA(graph, 2, 4), 2, "Should be 2")
        self.assertEqual(LCA.findLCA(graph, 4, 8), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(graph, 8, 4), 4, "Should be 4")
        self.assertEqual(LCA.findLCA(graph, 8, 5), 5, "Should be 5")
        self.assertEqual(LCA.findLCA(graph, 6, 9), 6, "Should be 6")
        self.assertEqual(LCA.findLCA(graph, 7, 9), 7, "Should be 7")


if __name__ == '__main__':
    unittest.main()