import unittest
import random
import dice_functions as dice


class test_dice_functions(unittest.TestCase):
    def test_dice_budget(self):
        self.assertEqual(
            dice.dice_budget(
                {'Plants': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]},
                [1, 1, 2, 3, 5, 6, 6], 7
            ),
            {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 2, 'dice_remaining': 7, 'dice_hand': [1, 1, 2, 3, 5, 6, 6]}
        )  # add assertion here

    def test_roll_dice(self):
        random.seed(123)
        self.assertEqual(
            dice.roll_dice(8, [2, 3]),
            [1, 3, 1, 4, 3, 1, 2, 3]
        )
        self.assertEqual(
            dice.roll_dice(8, []),
            [1, 4, 5, 5, 3, 3, 1, 2]
        )
        self.assertEqual(
            dice.roll_dice(8, [1, 2, 2, 3, 4, 5, 6, 6]),
            [1, 2, 2, 3, 4, 5, 6, 6]
        )

    def test_dice_count(self):
        self.assertEqual(
            dice.dice_count(5),
            8
        )

if __name__ == '__main__':
    unittest.main()
