import unittest

class InstuderingTest(unittest.TestCase):
	def test_goddag_return(self):
		self.assertEqual(goddag(), 'Goddag!')
    
	def test_string(self):
  		self.assertEqual(a, 'd')
  		self.assertEqual(b, 't')
  		self.assertEqual(c, 12)

	def test_hurra(self):
	    from io import StringIO
	    import sys
	    saved_stdout = sys.stdout
	    try:
	        out = StringIO()
	        sys.stdout = out
	        hurra()
	        output = out.getvalue().strip()
	        self.assertEqual(output, 
	        """Hipp Hipp
	          Hurra!
	          Hurra!
	          Hurra!""")
	    finally:
	        sys.stdout = saved_stdout