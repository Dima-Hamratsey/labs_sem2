import unittest
from queue_with_priority_lab4 import PriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.queue = PriorityQueue()

    def test_queue(self):
        self.assertIsNone(self.queue.hight_priority())
        self.queue.insert(7, 2)
        self.assertIsNotNone(self.queue.hight_priority())


if __name__ == '__main__':
    unittest.main()
