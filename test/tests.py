
import unittest
from exercise.exercise import add

class TestExercise(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5, "2 + 3 powinno być 5")

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, 1), 0, "-1 + 1 powinno być 0")

if __name__ == '__main__':
    unittest.main()