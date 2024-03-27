from typing import Any
import tokens
from SandyAi import decide as dm, dice as dice_func, modifiers as mod, scoring as score
import sys


def game_runner():
    #   initial modifier set up
    modifiers = {'Plants': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]},
    #   initial island settings
    #   TODO create an island class?
    islands = {
        1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
        2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0},
        3: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0},
        4: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0}
    }
    land_birds = 4
    current_round = 0
    tokens_held = None
    #   TODO make into a class for dice hand?
    dice: dict[str, list[Any] | int | Any] = {   #   make sure all uses of this are found
            'dice_amt': 6,
            'roll_result': [],
            'saved_dice': []
    }

    while current_round < 8:
        current_round += 1
        print(f"Round {current_round} has begun!\n")
        modifiers = mod.set_modifiers(islands)
        print("My modifiers are all set! Once you have set yours let's continue.\nIf its your turn to go first, Take "
              "your turn now and then you can tell me to go :)")
        player_turn()
        # sets dice based off of round number
        dice['dice_amt'] = dice_func.dice_count(current_round)
        dice['roll_result'] = dice_func.roll_dice(dice['dice_amt'], dice['saved_dice'])
        islands, land_birds, dice['saved_dice'], tokens_held = dm.spend_dice(islands, modifiers, dice, land_birds, tokens_held)
        tokens_held, dice['saved_dice'] = tokens.buy_tokens(tokens_held, dice['saved_dice'])
        print(f'End of round {current_round}\n')

    final_score = score.get_score(islands)
    print(f"Great game!!! My final score was {final_score}. I hope you had as much fun as I did. I'll be waiting for a "
          f"rematch!")


def player_turn():
    response = input("Enter 'Y' to continue or 'q' to quit the game.\n").strip().lower()
    if response == 'y':
        return
    elif response == 'q':
        sys.exit()
    else:
        print('Invalid response. Please enter "Y" to continue or "q" to quit the game.')
        player_turn()


if __name__ == '__main__':
    print(
        'Welcome to the Emerge AI.\n'
        'My name is Sandy and I will be playing Emerge along with you today. Let us begin!\n'
    )
    game_runner()
