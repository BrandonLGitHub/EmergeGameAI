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


if __name__ == '__main__':
    unittest.main()
