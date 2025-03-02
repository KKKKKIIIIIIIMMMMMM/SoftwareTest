import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        """Test numbers divisible by 3"""
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")
        self.assertEqual(fizzbuzz(12), "Fizz")

    def test_buzz(self):
        """Test numbers divisible by 5"""
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(20), "Buzz")
        self.assertEqual(fizzbuzz(25), "Buzz")

    def test_fizzbuzz(self):
        """Test numbers divisible by both 3 and 5"""
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(45), "FizzBuzz")
        self.assertEqual(fizzbuzz(60), "FizzBuzz")

    def test_regular_numbers(self):
        """Test numbers not divisible by 3 or 5"""
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz(4), 4)
        self.assertEqual(fizzbuzz(7), 7)
        self.assertEqual(fizzbuzz(11), 11)

    def test_edge_cases(self):
        """Test edge cases including negative numbers and zero"""
        self.assertEqual(fizzbuzz(0), "FizzBuzz")  # 0 is divisible by both 3 and 5
        self.assertEqual(fizzbuzz(-3), "Fizz")
        self.assertEqual(fizzbuzz(-5), "Buzz")
        self.assertEqual(fizzbuzz(-15), "FizzBuzz")
        self.assertEqual(fizzbuzz(-7), -7)
