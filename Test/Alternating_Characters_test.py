import unittest
from Alternating_Characters import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):
    def test_basic_cases(self):
        """Test basic alternating and non-alternating strings"""
        self.assertEqual(alternatingCharacters("AAAA"), 3)  # Need to delete 3 A's
        self.assertEqual(alternatingCharacters("BBBBB"), 4)  # Need to delete 4 B's
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)  # Already alternating
        self.assertEqual(alternatingCharacters("BABABA"), 0)  # Already alternating

    def test_mixed_cases(self):
        """Test strings with mixed patterns"""
        self.assertEqual(alternatingCharacters("AAABBB"), 4)  # Delete 2 A's and 2 B's
        self.assertEqual(alternatingCharacters("AABBAABB"), 4)  # Delete one from each pair
        self.assertEqual(alternatingCharacters("ABAABA"), 1)  # Delete one A

    def test_edge_cases(self):
        """Test edge cases including minimal length strings"""
        self.assertEqual(alternatingCharacters("A"), 0)  # Single character
        self.assertEqual(alternatingCharacters("AA"), 1)  # Two same characters
        self.assertEqual(alternatingCharacters("AB"), 0)  # Two different characters
        self.assertEqual(alternatingCharacters(""), 0)  # Empty string

    def test_special_patterns(self):
        """Test special patterns and longer sequences"""
        self.assertEqual(alternatingCharacters("AABAAB"), 2)  # Multiple groups
        self.assertEqual(alternatingCharacters("ABBABB"), 2)  # Multiple groups starting with A
        self.assertEqual(alternatingCharacters("ABABABAA"), 1)  # Good pattern with bad ending
