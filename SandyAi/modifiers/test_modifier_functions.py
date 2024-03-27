import unittest
import modifier_functions as mod


class test_modifier_functions(unittest.TestCase):

    def test_sort_dict_asc(self):
        self.assertEqual(
            mod.sort_dict_asc(
                {'Plants': 1, 'Seal': 4, 'Tectonic': 3, 'Bird': 2}
            ), [('Plants', 1), ('Bird', 2), ('Tectonic' ,3), ('Seal', 4)]
        )

    def test_sort_dict_dec(self):
        self.assertEqual(
            mod.sort_dict_dec(
                {'Plants': 1, 'Seal': 4, 'Tectonic': 3, 'Bird': 2}
            ), [('Seal', 4), ('Tectonic', 3), ('Bird', 2), ('Plants', 1)]
        )

    def test_extract_two_highest_values(self):
        self.assertEqual(
            mod.extract_two_highest_values(
                {'Plants': 2, 'Crab': 3, 'Seal': 4, 'Tectonic': 10, 'Bird': 6}
            ), ['Tectonic', 'Bird']
        )

    def test_extract_two_lowest_values(self):
        self.assertEqual(
            mod.extract_two_lowest_values(
                {'Plants': 2, 'Crab': 3, 'Seal': 4, 'Tectonic': 10, 'Bird': 6}
            ), ['Plants', 'Crab']
        )

    def test_set_modifiers(self):
        self.assertEqual(
            mod.set_modifiers(
                {1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
                 2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
                 3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
                 4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1}}
            ), {'Plants': [1], 'Crab': [], 'Turtle': [], 'Seal': [4], 'Tectonic': [5, 2], 'Bird': [6, 3]}
        )

if __name__ == '__main__':
    unittest.main()
