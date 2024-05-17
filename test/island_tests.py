import unittest
from src.island import floyd_warshall

class TestFloydWarshall(unittest.TestCase):
    def test_floyd_warshall(self):
        graph = [
            [0, 9, 75, 0, 0],
            [9, 0, 95, 19, 42],
            [75, 95, 0, 51, 66],
            [0, 19, 51, 0, 31],
            [0, 42, 66, 31, 0]
        ]
        expected_dist = [
            [0, 9, 51, 0, 0],
            [9, 0, 60, 9, 9],
            [51, 60, 0, 51, 51],
            [0, 9, 51, 0, 0],
            [0, 9, 51, 0, 0]
        ]
        dist, _ = floyd_warshall(graph)
        self.assertEqual(dist, expected_dist)

if __name__ == '__main__':
    unittest.main()
