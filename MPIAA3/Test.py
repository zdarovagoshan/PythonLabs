from DZ import AVLTree
import unittest


class BSTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def test_empty_tree(self):
        self.assertEqual(self.tree.search('Aleksandrova'), 'There is no such person')

    def test_insert_and_search(self):
        self.tree.insert(['Dori', 'Kovalcheck', '2', 'Mar', '1952'])
        self.assertEqual(self.tree.search('Kovalcheck'), 'Dori Kovalcheck 2 Mar 1952')

    def test_insert_and_search_more(self):
        self.tree.insert(['Dori', 'Kovalcheck', '2', 'Mar', '1952'])
        self.tree.insert(['Kasi', 'Hughett', '14', 'Nov', '1927'])
        self.tree.insert(['Kimberlie', 'Loncaric', '12', 'Sept', '1954'])
        self.assertEqual(self.tree.search('Hughett'), 'Kasi Hughett 14 Nov 1927')

    def test_balance(self):
        self.tree.insert(['Aleks', 'Akonechnikov', '4', 'Jun', '1997'])
        self.tree.insert(['Babka', 'Bozhko', '5', 'Mar', '1996'])
        self.tree.insert(['Vuasya', 'Durakov', '27', 'Sep', '1997'])
        self.assertEqual(self.tree.height, 1)


if __name__ == "__main__":
    unittest.main()
