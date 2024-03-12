import unittest
import decision_making as dm


class test_decision_making(unittest.TestCase):

    def test_update_dicehand(self):
        self.assertEqual(
            dm.update_dicehand(
                                'Bird', 2, [6, 6, 6, 1, 3],
                                {'Plants': [1], 'Crab': [2], 'Turtle': [3],
                                'Seal': [4], 'Tectonic': [5], 'Bird': [6]}
            ),
            [6, 1, 3]
        )
        self.assertEqual(
            dm.update_dicehand('Bird', 2, [6, 5, 6, 1, 3],
                               {'Plants': [1], 'Crab': [2], 'Turtle': [3],
                                'Seal': [4], 'Tectonic': [], 'Bird': [6, 5]}), [6, 1, 3]
        )

    def test_affordability(self):
        self.assertEqual(
            dm.affordability('Seal', 4,
                             {'Plants': 2, 'Crab': 1, 'Turtle': 0, 'Seal': 4, 'Tectonic': 0, 'Bird': 0,
                              'dice_remaining': 7, 'dice_hand': [1, 1, 2, 4, 4, 4, 4]}
                             ), True
        )
        self.assertEqual(
            dm.affordability('Seal', 4,
                             {'Plants': 2, 'Crab': 1, 'Turtle': 0, 'Seal': 2, 'Tectonic': 0, 'Bird': 0,
                              'dice_remaining': 7, 'dice_hand': [1, 1, 2, 4, 4, 4, 4]}
                             ), False
        )

    def test_check_cost(self):
        self.assertEqual(
            dm.check_cost('Tectonic', 1,
                          {
                              1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
                              2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
                              3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
                              4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
                          }, 2, None
                          ), 4
        )
        self.assertEqual(
            dm.check_cost('Bird', 1,
                          {
                              1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
                              2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
                              3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
                              4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
                          }, 2, None
                          ), 2
        )
        self.assertEqual(
            dm.check_cost('Bird', 1,
                          {
                              1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
                              2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
                              3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
                              4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
                          }, 0, None
                          ), 3
        )
        #   TODO add tests for tokens once that system is built out

    def test_update_board(self):

if __name__ == '__main__':
    unittest.main()
