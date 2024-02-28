from typing import Dict, List, Any

import decision_making as decide
import dice_functions as dice_func
import scoring as score


def game_runner():
    #   initial modifier set up
    modifiers = {'Plants': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]},
    #   initial island settings
    islands = {
        1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
        2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
        3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
        4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
    },
    land_birds = 4,
    current_round = 0
    dice: dict[str, list[Any] | int | Any] = {   #   make sure all uses of this are found
            'dice_amt': 6,
            'roll_result': [],
            'saved_dice': []
    }

    while current_round < 1:
        current_round += 1
        print(f"Round {current_round} has begun!\n")
        modifiers = decide.set_modifiers(modifiers, islands)
        # sets dice based off of round number subtracted by dice saved from last round
        dice['dice_amt'] = dice_func.dice_count(current_round) - len(dice['saved_dice'])
        dice['roll_result'] = dice_func.roll_dice(dice['dice_amt'], dice['saved_dice'])
        islands, land_birds = decide.spend_dice(islands, modifiers, dice, land_birds)
        print(f'End of round {current_round}')


if __name__ == '__main__':
    print(
        'Welcome to the Emerge AI.\n'
        'My name is Sandy and I will be playing Emerge along with you today. Let us begin!\n'
    )
    game_runner()
