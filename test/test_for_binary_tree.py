import unittest
from test_binary_tree import find_three_numbers

class TestFindThreeNumbers(unittest.TestCase):
    def test_case_1(self):
        arr = [1, 2, 3]
        P = 6
        self.assertTrue(find_three_numbers(arr, P))  # Очікуємо True

    def test_case_2(self):
        arr = [4, 5, 6, 7, 8]
        P = 15
        self.assertTrue(find_three_numbers(arr, P))  # Очікуємо True

    def test_case_3(self):
        arr = [1, 2, 3, 4, 5]
        P = 20
        self.assertFalse(find_three_numbers(arr, P))  # Очікуємо False

if __name__ == '__main__':
    unittest.main()
