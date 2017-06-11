from Backpack import Backpack
from item import Item
import DZ
import unittest

class BackpackTests(unittest.TestCase):
    def setUp(self):
        self.backpack = Backpack(7)
        self.backpack.clear()

    def test_empty(self):
        self.assertEqual(self.backpack.current_weight, 0)

    def test_insert(self):
        self.backpack.insert(Item('1', 2, 4))
        self.assertEqual(self.backpack.full_price, 4)
        self.assertEqual(self.backpack.current_weight, 2)
        self.assertEqual(self.backpack.items[0].name, '1')

    def test_clear(self):
        self.backpack.insert(Item('1', 2, 4))
        self.backpack.clear()
        self.assertEqual(self.backpack.full_price, 0)
        self.assertEqual(self.backpack.current_weight, 0)
        self.assertEqual(self.backpack.items, [])

    def test_greedy_alg(self):
        list_of_items = [Item('1', 2, 1), Item('2', 2, 3), Item('3', 3, 2), Item('4', 1, 1)]
        self.assertEqual(DZ.greedy(list_of_items, self.backpack), (7, 10))

    def test_standart_alg(self):
        list_of_items = [Item('1', 2, 1), Item('T.E.A.', 2, 3), Item('3', 3, 2), Item('4', 1, 1)]
        W = [list_of_items[i].weight for i in range(len(list_of_items))]
        P = [list_of_items[i].price for i in range(len(list_of_items))]
        self.assertEqual(DZ.standart(W, P, self.backpack, list_of_items), (7, 10))

if __name__ == "__main__":
    unittest.main()
