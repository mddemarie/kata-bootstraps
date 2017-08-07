import unittest


class TodoProjectNameTestCase(unittest.TestCase):
    '''Tests for .py'''
    def test_name_of_test(self):
        """It succesfully does this."""
        positive_number = 2
        self.assertEqual(positive_number, 2)


if __name__ == '__main__':
    unittest.main()
