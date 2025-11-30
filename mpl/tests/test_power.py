import lib1
import unittest

class TestPower(unittest.TestCase):
    def test_0(self):
        self.assertEqual(lib1.my_power(3,0), 1)
    def test_1(self):
        self.assertEqual(lib1.my_power(3,1), 3)
    def test_2(self):
        self.assertEqual(lib1.my_power(3,2), 9)
    def test__1(self):
        self.assertEqual(lib1.my_power(3,-1), 1/3)    
    
if __name__ == '__main__':
    unittest.main()
