import unittest

class StringTests(unittest.TestCase):
  def test_a_is_P(self):
    self.assertEqual(a, 'P')
  
  def test_b_is_t(self):
    self.assertEqual(b, 't')
  
  def test_c_is_n(self):
    self.assertEqual(c, 'n')
  
  def test_d_is_ytho(self):
    self.assertEqual(d, 'ytho')
  
  def test_e_is_len(self):
    self.assertEqual(e, 6)
  
  def test_is_s_a_string(self):
    self.assertTrue(isinstance(s, str))
    
  