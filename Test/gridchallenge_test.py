import unittest
from gridchallenge import gridChallenge

class TestGridChallenge(unittest.TestCase):
    def test_valid_grids(self):
        """Test grids that can be arranged to satisfy the conditions"""
        self.assertEqual(gridChallenge(['abc', 'def', 'ghi']), 'YES')  # Already sorted
        self.assertEqual(gridChallenge(['cba', 'fed', 'ihg']), 'YES')  # Needs sorting but valid
        self.assertEqual(gridChallenge(['abc', 'lmp', 'qrt']), 'YES')  # Valid after sorting
        self.assertEqual(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']), 'YES')

    def test_invalid_grids(self):
        """Test grids that cannot be arranged to satisfy the conditions"""
        self.assertEqual(gridChallenge(['zyx', 'wvu', 'tsr']), 'NO')  # Invalid after sorting
        self.assertEqual(gridChallenge(['mpxz', 'abcd', 'wlmb']), 'NO')  # Cannot be sorted properly
        self.assertEqual(gridChallenge(['abc', 'hjk', 'def']), 'NO')  # Middle row too high

    def test_edge_cases(self):
        """Test edge cases including empty and single-element grids"""
        self.assertEqual(gridChallenge([]), 'NO')  # Empty grid
        self.assertEqual(gridChallenge(['a']), 'YES')  # Single character
        self.assertEqual(gridChallenge(['ab', 'cd']), 'YES')  # 2x2 grid
        self.assertEqual(gridChallenge(['z']), 'YES')  # Single character, last letter

    def test_invalid_dimensions(self):
        """Test grids with invalid dimensions"""
        self.assertEqual(gridChallenge(['abc', 'de']), 'NO')  # Different row lengths
        self.assertEqual(gridChallenge(['a', 'ab', 'abc']), 'NO')  # Increasing row lengths
        self.assertEqual(gridChallenge(['abc', '', 'def']), 'NO')  # Empty row

    def test_special_cases(self):
        """Test special cases with repeated characters"""
        self.assertEqual(gridChallenge(['aaa', 'aaa', 'aaa']), 'YES')  # All same character
        self.assertEqual(gridChallenge(['abc', 'abc', 'abc']), 'YES')  # Repeated rows
        self.assertEqual(gridChallenge(['zzz', 'aaa', 'zzz']), 'NO')  # Invalid with repeats
