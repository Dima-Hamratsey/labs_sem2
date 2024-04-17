
from main import find_way_robot
import unittest


class TestOfRobotsWays(unittest.TestCase):

    def test_1(self):
        """
        Поле розміром m==n==5
        """
        field_1 = [[1, 2, 3, 4, 5],
                                 [6, 7, 8, 9, 10],
                                 [11, 12, 13, 14, 15],
                                 [16, 17, 18, 19, 20],
                                 [21, 22, 23, 24, 25]]

        expected_result = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25]
        self.assertEqual(find_way_robot(field_1), expected_result)

    def test_2(self):
        """
        Поле розміром m = 2, n = 4
        """
        field_2 = [[1, 2, 3, 4],
                                 [5, 6, 7, 8]]

        expected_result = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(find_way_robot(field_2), expected_result)

    def test_3(self):
        """
        Поле розміром n = 1, m = 6
        """
        field_3 = [[1],
                                 [7],
                                 [11],
                                 [16],
                                 [1],
                                 [12]]

        expected_result = [1, 7, 11, 16, 1, 12]
        self.assertEqual(find_way_robot(field_3), expected_result)
