import random
import copy
from typing import List
#   import decision-making functions
#   import dice functions
#   import scoring functions

def game_runner():
    current_board = {
        #   initial modifier set up
        'modifiers': {'Plants': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]},
        #   initial island settings
        'islands': {
            1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
            2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
            3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
            4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
        },
        'land_birds': 4,
        'score': 0,
        'round': 0,
        'dice_amt': 6,
        'roll_result': [],
        'saved_dice': []
    }
    while current_board['round'] < 1:
        current_board['round'] += 1
        print(f"Round {current_board['round']} has begun!\n")
        current_board['modifiers'] = set_modifiers(current_board)
        # sets dice based off of round number subtracted by dice saved from last round
        current_board['dice_amt'] = dice_count(current_board['round']) - len(current_board['saved_dice'])
        current_board['roll_result'] = roll_dice(current_board['dice_amt'], current_board['saved_dice'])
        current_board['islands'] = spend_dice(current_board)
        print(f'End of round {current_board["round"]}')


if __name__ == '__main__':
    print(
        'Welcome to the Emerge AI.\n'
        'My name is Sandy and I will be playing Emerge along with you today. Let us begin!\n'
    )
    game_runner()
