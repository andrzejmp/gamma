import lib
import unittest


class TestPrimeFunction(unittest.TestCase):
    def test_1(self):
        self.assertEqual(lib.prime(1), False)
    def test_2(self):
        self.assertEqual(lib.prime(2), True)
    def test_3(self):
        self.assertEqual(lib.prime(4), False)
    def test_4(self):    
        self.assertEqual(lib.prime(12), False)
    def test_5(self):    
        self.assertEqual(lib.prime(10), False)
    def test_100(self):    
        self.assertEqual(lib.prime(100), False)
    def test_0(self):    
        self.assertEqual(lib.prime(0), False)
    def test_19(self):    
        self.assertEqual(lib.prime(19), True)    
        


if __name__ == '__main__':
    unittest.main()
