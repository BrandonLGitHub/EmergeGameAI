import unittest
from scoring import scoring as score


class test_scoring(unittest.TestCase):

    def test_get_score(self):
        self.assertEqual(
            score.get_score(
                {
                    1: {'Plants': 2, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 3, 'Bird': 1},
                    2: {'Plants': 1, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
                    3: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0},
                    4: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0}
                }
            ), 15
        )

    def test_island_score(self):
        self.assertEqual(
            score.island_score({'Plants': 2, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 3, 'Bird': 1}),
            12
        )
        self.assertEqual(
            score.island_score({'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0}),
            0
        )
        self.assertEqual(
            score.island_score({'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 1, 'Tectonic': 1, 'Bird': 1}),
            9
        )

if __name__ == '__main__':
    unittest.main()