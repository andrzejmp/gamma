import lib1
import unittest

class TestPrimeFunction(unittest.TestCase):
    def test_1(self):
        self.assertEqual(lib1.checkTriangle(1,1,1), True)
    def test_2(self):
        self.assertEqual(lib1.checkTriangle(3,4,5), True)
    def test_3(self):
        self.assertEqual(lib1.checkTriangle(3,3,10), False)
    
if __name__ == '__main__':
    unittest.main()

