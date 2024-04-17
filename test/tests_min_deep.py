import unittest
from main import has_cycle

class TestCycleDetection(unittest.TestCase):
    def test_has_cycle_function_runs(self):
        graph = {
            1: [2, 3],
            2: [1, 3, 5],
            3: [1, 2, 4],
            4: [3, 5],
            5: [2, 4]
        }

        try:
            has_cycle(graph)
        except Exception as e:
            self.fail(f"Function has_cycle() raised an unexpected exception: {e}")

if __name__ == "__main__":
    unittest.main()
