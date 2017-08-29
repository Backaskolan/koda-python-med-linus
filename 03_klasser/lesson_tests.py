import unittest

class ClassTests(unittest.TestCase):
  def setUp(self):
    self.test_instance = Sak('test', 'test')
    
  def test_penna_is_sak(self):
    self.assertTrue(isinstance(self.test_instance, Sak)
    
  def test_vars_are_strings(self):
    self.assertTrue(type(self.test_instance.namn) == str)
    self.assertTrue(type(self.test_instance.beskrivning) == str)
    