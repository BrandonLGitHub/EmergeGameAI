import unittest
import move_forecasting as forecast

class test_move_forecasting(unittest.TestCase):

    def test_check_moves(self):
        self.assertEqual(
            forecast.check_moves(
                            {
                    1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
                    2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
                    3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
                    4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
                }
            ),
            {
                1: {'Plants': True, 'Crab': True, 'Turtle': False, 'Seal': False, 'Tectonic': True, 'Bird': True},
                2: {'Plants': True, 'Crab': False, 'Turtle': False, 'Seal': False, 'Tectonic': True, 'Bird': True},
                3: {'Plants': False, 'Crab': False, 'Turtle': True, 'Seal': False, 'Tectonic': True, 'Bird': True},
                4: {'Plants': True, 'Crab': False, 'Turtle': False, 'Seal': True, 'Tectonic': True, 'Bird': False},
            }
        )
        self.assertEqual(
            forecast.check_moves(
                {1: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0}}
            ),  {1: {'Plants': False, 'Crab': False, 'Turtle': False, 'Seal': False, 'Tectonic': True, 'Bird': False}}
        )
        self.assertEqual(
            forecast.check_moves(
                {1: {'Plants': 3, 'Crab': 1, 'Turtle': 1, 'Seal': 1, 'Tectonic': 3, 'Bird': 1}}
            ), {1: {'Plants': False, 'Crab': False, 'Turtle': False, 'Seal': False, 'Tectonic': False, 'Bird': False}}
        )

    def test_weigh_moves(self):
        self.assertEqual(
            forecast.weigh_moves({1: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0}}),
            {1: {'Tectonic': 1}}
        )
        self.assertEqual(
            forecast.weigh_moves(
                {
                    1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
                    2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
                    3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
                    4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1}
                }
            ), {
                1: {'Plants': 1, 'Crab': 1, 'Tectonic': 1, 'Bird': 2},
                2: {'Plants': 1, 'Tectonic': 0, 'Bird': 2},
                3: {'Turtle': 1, 'Tectonic': 4, 'Bird': 2},
                4: {'Plants': 1, 'Seal': 4, 'Tectonic': 5}
            }
        )