import ad
import unittest

class TestAdding(unittest.TestCase):
    def test_0(self):
        self.assertEqual(ad.add(1,1), 2)
    def test_1(self):
        self.assertEqual(ad.add(-2,2), 0)
    def test_2(self):
        self.assertEqual(ad.add(3,2), 5)
       
    
if __name__ == '__main__':
    unittest.main()
