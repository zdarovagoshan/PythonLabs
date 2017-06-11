from graph import Graph
import unittest


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_empty(self):
        self.assertEqual(self.graph.get_vertices(), [])

    def test_add_edge(self):
        self.graph.add_edge("A", "B")
        self.assertEqual(len(self.graph.get_vertices()), 2)
        self.assertTrue(self.graph.has_edge("A", "B"))
        self.assertIn("B", self.graph.get_adjacent("A"))
        self.assertEqual(self.graph.krascal_alg(), [('A', 'B', 1)])

    def test_add_edges(self):
        self.graph.add_edge("A", "B")
        self.graph.add_edge("A", "C")
        self.graph.add_vertex("D")
        self.assertEqual(len(self.graph.get_vertices()), 4)
        self.assertIn("C", self.graph.get_adjacent("A"))
        self.assertNotIn("D", self.graph.get_adjacent("A"))
        self.assertFalse(self.graph.has_edge("A", "D"))

    def test_krascal_alg(self):
        self.graph.add_edge('0', '1', 1)
        self.graph.add_edge('1', '0', 2)
        self.graph.add_edge('1', '3', 8)
        self.graph.add_edge('1', '2', 6)
        self.graph.add_edge("3", "2", 4)
        self.graph.add_edge("3", "4", 5)
        self.graph.add_edge("5", "6", 9)
        self.graph.add_edge("4", "6", 8)
        self.graph.add_edge("3", "5", 2)
        self.graph.add_edge("8", "4", 1)
        self.graph.add_edge("7", "4", 7)
        self.assertEqual(self.graph.krascal_alg(), [('4','8',1), ('3','5',2), ('0', '1', 3), ('2','3',4), ('3','4',5), ('1', '2', 6), ('4','7',7), ('4','6',8)])

    def test_weight(self):
        self.graph.add_edge('0', '1', 1)
        self.graph.add_edge('1', '0', 2)
        self.graph.add_edge('1', '3', 8)
        self.graph.add_edge('1', '2', 6)
        self.graph.add_edge("3", "2", 4)
        self.graph.add_edge("3", "4", 5)
        self.graph.add_edge("5", "6", 9)
        self.graph.add_edge("4", "6", 8)
        self.graph.add_edge("3", "5", 2)
        self.graph.add_edge("8", "4", 1)
        self.graph.add_edge("7", "4", 7)
        self.assertEqual(self.graph.get_weight(), 53)


if __name__ == "__main__":
    unittest.main()
