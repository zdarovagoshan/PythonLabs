import unittest
import DZ

pustos=[]

class MyTestCase(unittest.TestCase):
    def test_DZ(self):
        self.assertEqual(DZ.insertion_sort([]), pustos)
    def test_DZ2(self):
        self.assertEqual(DZ.bucket_sort([]), pustos)
    def test_ins(self):
        self.assertEqual(DZ.insertion_sort(['Keena Mith 19 Dec 1977', 'Keena Ya 10 May 1979']), ['Keena Ya 10 May 1979','Keena Mith 19 Dec 1977'])
    def test_ins2(self):
        self.assertEqual(DZ.insertion_sort(['Deirdre Recore 31 Jan 1945', 'Andre Londono 20 Sept 1987']), ['Andre Londono 20 Sept 1987','Deirdre Recore 31 Jan 1945'])
    def test_buc2(self):
        self.assertEqual(DZ.bucket_sort(['Deirdre Recore 31 Jan 1945', 'Andre Londono 20 Sept 1987']), ['Andre Londono 20 Sept 1987', 'Deirdre Recore 31 Jan 1945'])

if __name__ == '__main__':
    unittest.main()
