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
            ), (1, [])
        )
        self.assertEqual(
            tokens.use_token(
                tokens_held, 'Bird', 'cost'
            ), (None, tokens_held)
        )

    def test_use_token_for_cost(self):
        tokens_held = [tokens.research_token('Crab', 1, 'cost', 1,
                                             'Place a crab for 1 die.')]
        self.assertEqual(
            tokens.use_token_for_cost(tokens_held, 'Crab'),
            (1, [])
        )


    def test_get_feature(self):
        with patch('builtins.input', return_value='1'):
            self.assertEqual(
                tokens.get_feature(), 'Plants'
            )

    def test_get_num(self):
        token_bank = tokens.generate_bank()
        with patch('builtins.input', return_value='1'):
            self.assertEqual(
                tokens.get_num('Crab', token_bank), 1
            )

    def test_buy_tokens(self):
        token_bank = tokens.generate_bank()
        crab1 = tokens.research_token('Crab', 1, 'cost', 1, 'Place a crab for 1 die.')
        bird3 = tokens.research_token('Bird', 3, 'Tectonic', None,
                                      'When you steal a Bird, grown the island it lands on.')
        with patch('builtins.input', side_effect=['2', '1', '5', '3']):
            self.assertEqual(
                tokens.buy_tokens([], 4, token_bank),
                ([crab1, bird3], 0)
            )

    def test_extract_token(self):
        token_bank = tokens.generate_bank()
        self.assertEqual(
            tokens.extract_token(token_bank, "Plants", '1')
        )

if __name__ == '__main__':
    unittest.main()
