import unittest
from Caesar_Cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):
    def test_basic_lowercase(self):
        """Test basic lowercase letter shifts"""
        self.assertEqual(caesarCipher("abc", 1), "bcd")
        self.assertEqual(caesarCipher("xyz", 1), "yza")
        self.assertEqual(caesarCipher("abc", 2), "cde")
        self.assertEqual(caesarCipher("abc", 25), "zab")

    def test_basic_uppercase(self):
        """Test basic uppercase letter shifts"""
        self.assertEqual(caesarCipher("ABC", 1), "BCD")
        self.assertEqual(caesarCipher("XYZ", 1), "YZA")
        self.assertEqual(caesarCipher("ABC", 2), "CDE")
        self.assertEqual(caesarCipher("ABC", 25), "ZAB")

    def test_mixed_case(self):
        """Test strings with mixed case letters"""
        self.assertEqual(caesarCipher("aBcDeF", 1), "bCdEfG")
        self.assertEqual(caesarCipher("xYzAbC", 2), "zAbCdE")  # Fixed expected output to match case preservation
        self.assertEqual(caesarCipher("Hello", 3), "Khoor")

    def test_special_characters(self):
        """Test strings with non-alphabetic characters"""
        self.assertEqual(caesarCipher("abc123", 1), "bcd123")
        self.assertEqual(caesarCipher("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(caesarCipher("123!@#", 5), "123!@#")
        self.assertEqual(caesarCipher(" ", 10), " ")

    def test_large_shifts(self):
        """Test shifts larger than 26"""
        self.assertEqual(caesarCipher("abc", 26), "abc")  # Full rotation
        self.assertEqual(caesarCipher("xyz", 27), "yza")  # 27 = 1 (mod 26)
        self.assertEqual(caesarCipher("ABC", 52), "ABC")  # Two full rotations
        self.assertEqual(caesarCipher("Hello", 55), "Khoor")  # 55 = 3 (mod 26)

    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(caesarCipher("", 5), "")  # Empty string
        self.assertEqual(caesarCipher("abc", 0), "abc")  # No shift
        self.assertEqual(caesarCipher("!@#$%^&*()", 10), "!@#$%^&*()")  # Only special characters
        self.assertEqual(caesarCipher("aAaA", 1), "bBbB")  # Alternating case

if __name__ == '__main__':
    unittest.main() 