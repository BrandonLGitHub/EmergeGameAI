import unittest
import decision_making as dm


class test_decision_making(unittest.TestCase):

    def test_update_dicehand(self):
        self.assertEqual(
            dm.update_dicehand(
                'Bird', 2, [6, 6, 6, 1, 3],
                {'Plants': [1], 'Crab': [2], 'Turtle': [3],
                 'Seal': [4], 'Tectonic': [5], 'Bird': [6]}
            ), [6, 1, 3]
        )
        self.assertEqual(
            dm.update_dicehand(
                'Bird', 2, [6, 5, 6, 1, 3],
                {'Plants': [1], 'Crab': [2], 'Turtle': [3],
                 'Seal': [4], 'Tectonic': [], 'Bird': [6, 5]}
            ), [6, 1, 3]
        )


if __name__ == '__main__':
    unittest.main()