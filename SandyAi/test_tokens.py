import unittest
import tokens

class test_tokens(unittest.TestCase):
    def test_use_token(self):
        tokens_held = [tokens.research_token('Crab', 1, 'cost', 1,
                                       'Place a crab for 1 die.')]
        self.assertEqual(
            tokens.use_token(
                tokens_held, 'Crab', 'cost'
            ), (1,[])
        )
        self.assertEqual(
            tokens.use_token(
                tokens_held, 'Crab', 'cost'
            ), (None,tokens_held)
        )


if __name__ == '__main__':
    unittest.main()
