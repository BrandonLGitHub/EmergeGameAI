import unittest
from unittest.mock import patch
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
                tokens_held, 'Bird', 'cost'
            ), (None,tokens_held)
        )

    def test_use_token_for_cost(self):
        tokens_held = [tokens.research_token('Crab', 1, 'cost', 1,
                                             'Place a crab for 1 die.')]
        self.assertEqual(
            tokens.use_token_for_cost(tokens_held, 'Crab'),
            (1,[])
        )

    def test_buy_tokens(self):
        token_bank = tokens.generate_bank()
        self.assertEqual(
            tokens.buy_tokens([],4, token_bank),
            ([],0)
        )
if __name__ == '__main__':
    unittest.main()
