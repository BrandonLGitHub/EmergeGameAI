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
        self.assertEqual(
            dm.check_cost('Plants', 1,
                          {
                              1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
                              2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
                              3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
                              4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
                          }, 2, None
                          ), 2
        )

        #   TODO add tests for tokens once that system is built out

    def test_update_board(self):
        dm.update_board('Crab', 1, {
            1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
        }, 1, None), (
            {
                1: {'Plants': 2, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 1},
            }, 1, None
        )
        dm.update_board('Bird', 1, {
            1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
        }, 1, None), (
            {
                1: {'Plants': 2, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 1},
            }, 0, None
        )
        dm.update_board('Bird', 1, {
            1: {'Plants': 4, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
        }, 1, None), (
            {
                1: {'Plants': 4, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 1},
            }, 0, None
        )
        dm.update_board('Tectonic', 1, {
            1: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0},
        }, 1, None), (
            {
                1: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
            }, 1, None
        )

    def test_spend_dice(self):
        self.assertEqual(
            dm.spend_dice(
                {
                    1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
                    2: {'Plants': 2, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 1}
                }, {'Plants': [1], 'Crab': [2], 'Turtle': [], 'Seal': [], 'Tectonic': [5, 4], 'Bird': [6, 3]},
                {'dice_amt': 8,
                 'roll_result': [5, 4, 5, 6, 6, 3, 1, 3],
                 'saved_dice': []}, 0, None
            ), (
                {
                    1: {'Plants': 2, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 1},
                    2: {'Plants': 2, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 1}
                }, 0, None, None
            )
        )

    def test_update_budget(self):
        self.assertEqual(
            dm.update_budget(
                'Tectonic', 3,
                {'Plants': 2, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 3, 'Bird': 0,
                 'dice_remaining': 6, 'dice_hand': [1, 1, 2, 5, 5, 5]},
                {'Plants': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]}
            ), {'Plants': 2, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0,
                'dice_remaining': 3, 'dice_hand': [1, 1, 2]}
        )


if __name__ == '__main__':
    unittest.main()
