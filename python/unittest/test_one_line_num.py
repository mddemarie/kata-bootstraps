import unittest
import one_line_num


class TodoProjectNameTestCase(unittest.TestCase):
    '''Tests for one_line_num.py'''
    def test_print_positive_number(self):
        """It succesfully prints any positive number."""
        positive_number = 7
        result = one_line_num.number_per_line(positive_number)
        self.assertEqual(result, 7)

    def test_print_fizz_for_three_divides(self):
        """It prints fizz if I pass a number that I can divide by 3."""
        number_three = 9
        result = one_line_num.number_per_line(number_three)
        self.assertEqual(result, "fizz")

    def test_print_buzz_for_five_divides(self):
        """It prints buzz if I pass a number that I can divide by 5."""
        number_five = 10
        result = one_line_num.number_per_line(number_five)
        self.assertEqual(result, "buzz")

    def test_print_fizzbuzz_for_five_and_three_divides(self):
        """It prints fizzbuzz if I pass a number that I can \
        divide by 3 and 5."""
        number_five_three = 15
        result = one_line_num.number_per_line(number_five_three)
        self.assertEqual(result, "FizzBuzz")

    def test_positive_number_not_bigger_than_100(self):
        """It gives an ValueError if the number is higher than 100."""
        higher_number = 145
        with self.assertRaises(ValueError):
            one_line_num.number_per_line(higher_number)

    def test_passing_zero(self):
        """It gives an ValueError if the number is 0."""
        zero_number = 0
        with self.assertRaises(ValueError):
            one_line_num.number_per_line(zero_number)

    def test_passing_negative_number(self):
        """It gives an ValueError if the number is smaller than 0."""
        negative_number = -5
        with self.assertRaises(ValueError):
            one_line_num.number_per_line(negative_number)

    def test_passing_string(self):
        """It gives an TypeError if the number is a string."""
        missing_number = "doggie"
        with self.assertRaises(TypeError):
            one_line_num.number_per_line(missing_number)


if __name__ == '__main__':
    unittest.main()
