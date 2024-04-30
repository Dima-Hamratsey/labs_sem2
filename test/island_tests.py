import unittest
from islands import min_cable_length

class TestMinCableLength(unittest.TestCase):

    def test_empty_graph(self):
        graph = []
        expected_length = 0
        self.assertEqual(min_cable_length(graph), expected_length)

    def test_single_island(self):
        graph = [[0]]
        expected_length = 0
        self.assertEqual(min_cable_length(graph), expected_length)

    def test_two_islands(self):
        graph = [
            [0, 1],
            [1, 0]
        ]
        expected_length = 1
        self.assertEqual(min_cable_length(graph), expected_length)

    def test_three_islands(self):
        graph = [
            [0, 1, 2],
            [1, 0, 3],
            [2, 3, 0]
        ]
        expected_length = 3
        self.assertEqual(min_cable_length(graph), expected_length)

if __name__ == '__main__':
    unittest.main()
