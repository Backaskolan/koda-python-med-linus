class AdditionTests(unittest.TestCase):
    def test_sub_is_a_function(self):
        self.assertTrue(callable(sub))
    def test_subs_two_positive_numbers(self):
        self.assertEqual(sub(1, 1), 0)
