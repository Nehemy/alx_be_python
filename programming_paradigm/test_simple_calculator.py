from simple_calculator import SimpleCalculator
import unittest


class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(5,8), 13)
        self.assertEqual(self.calc.add(-2,19), 17) 
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,8), -3)
        self.assertEqual(self.calc.subtract(-2,19), -21) 
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,8), 40)
        self.assertEqual(self.calc.multiply(-2,19), -38) 
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10,5), 2.0)
        self.assertEqual(self.calc.divide(5,5), 1.0)