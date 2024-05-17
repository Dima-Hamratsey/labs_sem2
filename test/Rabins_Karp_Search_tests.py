import os
import sys
test_file_path = os.path.abspath(file)
common_parent_path = os.path.abspath(os.path.join(os.path.dirname(test_file_path), os.pardir))
src_path = os.path.join(common_parent_path, 'src')
sys.path.append(src_path)
import unittest
from Rabin_Karp_Search import rabin_karp_search

class TestRabinKarp(unittest.TestCase):

    def test_pattern_present(self):
        haystack = "ababcababc"
        needle = "abc"
        self.assertEqual(rabin_karp_search(haystack, needle), [2, 7])

    def test_pattern_not_present(self):
        haystack = "ababcababc"
        needle = "xyz"
        self.assertEqual(rabin_karp_search(haystack, needle), [])

    def test_empty_pattern(self):
        haystack = "ababcababc"
        needle = ""
        self.assertEqual(rabin_karp_search(haystack, needle), [])

    def test_pattern_in_empty_text(self):
        haystack = ""
        needle = "abc"
        self.assertEqual(rabin_karp_search(haystack, needle), [])

if __name__ == '__main__':
    unittest.main()
