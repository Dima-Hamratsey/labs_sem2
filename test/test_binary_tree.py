import unittest
from level3 import BinaryTree, find_successor

class TestFindSuccessor(unittest.TestCase):
    def test_find_successor(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(15)
        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)
        root.right.right = BinaryTree(20)
        root.right.right.left = BinaryTree(12)

        node_7 = root.left.right

        expected_successor_value = 10

        successor_node = find_successor(root, node_7)

        self.assertEqual(successor_node.value, expected_successor_value)

if __name__ == '__main__':
    unittest.main()
