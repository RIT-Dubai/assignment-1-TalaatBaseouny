import unittest

class draw_square(unittest.TestCase):


    def test_draw_square(self):
        self.assertEqual('90,90,90,90'.upper(), '90,90,90,90')

def test_draw_square(self):
        self.assertTrue('90,90,90,90'.isupper())
        self.assertFalse('90,90,90,90'.isupper())
