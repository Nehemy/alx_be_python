from simple_calculator import SimpleCalculator
import unittest

operation = SimpleCalculator()


class TestSimpleCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(operation.add(5,8), 13)
        self.assertEqual(operation.add(-2,19), 17) 
        
    def test_subtract(self):
        self.assertEqual(operation.subtract(5,8), -3)
        self.assertEqual(operation.subtract(-2,19), -21) 
    
    def test_multiply(self):
        self.assertEqual(operation.multiply(5,8), 40)
        self.assertEqual(operation.multiply(-2,19), -38) 
    
    def test_divide(self):
        self.assertEqual(operation.divide(10,5), 2.0)
        self.assertEqual(operation.divide(5,5), 1.0)