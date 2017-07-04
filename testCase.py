import unittest
from number_gen import prime_gen

class PrimesTestCase(unittest.TestCase):

    def test_negative_input(self):
        self.assertFalse(prime_gen(-1),msg = 'should not be negative')

    def test_alphabetical_input(self):
        self.assertFalse(prime_gen('a'),msg = 'should be positive number')

    def test_float_value_input(self):
        self.assertFalse(prime_gen(2.0),msg = 'should be positive int') 

    def test_list_input(self):
        self.assertFalse(prime_gen([2]), msg = 'Should not be a list') 
        
    def test_set_input(self):
        self.assertFalse(prime_gen({-1}),msg = 'should be negative')            



if __name__ == '__main__':
    unittest.main()        
