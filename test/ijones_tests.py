import unittest
from ijones import ijones


class TestIJones(unittest.TestCase):
    def test_ijones_input(self):
        ijones('ijones.in', 'ijones.out')
        with open('ijones.out', 'r') as file:
            expected_result = file.readline().strip()

if __name__ == '__main__':
    unittest.main()
