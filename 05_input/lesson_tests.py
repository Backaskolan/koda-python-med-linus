import unittest

class InputTest(unittest.TestCase):
  def test_answer_is_int(self):
    self.assertTrue(isinstance(add("3", "4"), int), "\n*** FEL ***\nSvaret är en textsträng, inte ett tal!")
    
