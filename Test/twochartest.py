import unittest
from twochar import alternate

class TestAlternate(unittest.TestCase):
    def test_basic_alternating(self):
        """Test basic alternating sequences"""
        self.assertEqual(alternate("abab"), 4)  # Perfect alternating sequence
        self.assertEqual(alternate("baba"), 4)  # Perfect alternating sequence reversed
        self.assertEqual(alternate("beabeefeab"), 5)  # Multiple characters, longest is 'babab'

    def test_invalid_sequences(self):
        """Test sequences that contain invalid alternations"""
        self.assertEqual(alternate("aaa"), 0)  # Same character repeated
        self.assertEqual(alternate("aabb"), 0)  # No valid alternating sequence
        self.assertEqual(alternate("abaaab"), 0)  # Contains invalid sequence (consecutive a's)

    def test_edge_cases(self):
        """Test edge cases including minimal strings"""
        self.assertEqual(alternate(""), 0)  # Empty string
        self.assertEqual(alternate("a"), 0)  # Single character
        self.assertEqual(alternate("ab"), 2)  # Minimum valid sequence
        self.assertEqual(alternate("abc"), 2)  # More than two unique chars, but only use two

    def test_complex_sequences(self):
        """Test more complex sequences"""
        self.assertEqual(alternate("abcdef"), 2)  # Many chars but can only use two
        self.assertEqual(alternate("abababab"), 8)  # Long alternating sequence
        self.assertEqual(alternate("cdcdcdcdeeeef"), 8)  # Multiple valid sequences, find longest
        self.assertEqual(alternate("xxyy"), 0)  # No valid alternating sequence

    def test_special_cases(self):
        """Test special cases with multiple valid possibilities"""
        self.assertEqual(alternate("beabeefeab"), 5)  # Can form 'babab'
        self.assertEqual(alternate("asdcbsdcagfestfestwaefccsd"), 5)  # Multiple possibilities
        self.assertEqual(alternate("ZXzxZXzx"), 4)  # Case-sensitive alternating (can form 'ZXZX' or 'zxzx')
