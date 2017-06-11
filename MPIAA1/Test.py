import unittest
import DZ


class MyTestCase(unittest.TestCase):
    def test_DZ(self):
        self.assertEqual(DZ.find([]), [])
    def test_sravn(self):
        self.assertEqual(DZ.find(["Alexander Call 5 Nov 1979"]), [])
    def test_sravn2(self):
        self.assertEqual(DZ.find(["Elene Entsminger 1 Apr 1905"]), ["Elene Entsminger 1 Apr 1905"])
    def test_sravn3(self):
        test4 = DZ.read_file("test4.txt".format(2))
        self.assertEqual(DZ.find(test4), ["Elene Entsminger 1 Apr 1905", "Kent Kessler 26 Dec 1952"])

if __name__ == '__main__':
    unittest.main()
