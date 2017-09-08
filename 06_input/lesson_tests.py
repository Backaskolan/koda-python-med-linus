import unittest

class InputTest(unittest.TestCase):
  def test_answer_is_int(self):
    self.assertTrue(type(add("3", "4")) is int, "\n*** FEL ***\nSvaret är en textsträng, inte ett tal!")
    
