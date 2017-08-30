import unittest

class MultAndDivTests(unittest.TestCase):
  def test_mult_is_a_function(self):
    self.assertTrue(callable(mult))
  def test_div_is_a_function(self):
    self.assertTrue(callable(div))
  def test_mult_multiplies_two_numbers(self):
    self.assertEqual(mult(3, 4), 12)
  def test_div_divides_two_numbers(self):
    self.assertEqual(div(12, 3), 4)
    