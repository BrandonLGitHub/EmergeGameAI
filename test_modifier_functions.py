import unittest
import modifier_functions as mod


class test_modifier_functions(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(
            mod.flatten(
                {
                    1: {"Plants": 2, "Crabs": 1},
                    2: {"Plants": 1, "Crabs": 0}
                }
            ), {"Plants": 2, "Crabs": 1, "Plants": 1, "Crabs": 0}
        )  # add assertion here

    def test_sort_dict_asc(self):
        self.assertEqual(
            mod.sort_dict_asc(
                {'Plants': 1, 'Seal': 4, 'Tectonic': 3, 'Bird': 2}
            ), [('Plants', 1), ('Bird', 2), ('Tectonic' ,3), ('Seal', 4)]
        )

if __name__ == '__main__':
    unittest.main()
