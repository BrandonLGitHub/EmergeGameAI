from typing import Any
import SandyAi.tokens as tokens
from SandyAi import decide as dm, dice as dice_func, modifiers as mod, scoring as score, tokens


# TODO docstrings
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
    tokens_held = []
    token_bank = tokens.generate_bank()
    dice: dict[str, list[Any] | int | Any] = {
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
        dm.player_turn()
        # sets dice based off of round number
        dice['dice_amt'] = dice_func.dice_count(current_round)
        dice['roll_result'] = dice_func.roll_dice(dice['dice_amt'], dice['saved_dice'])
        islands, land_birds, dice['saved_dice'], tokens_held = dm.spend_dice(islands, modifiers, dice, land_birds,
                                                                             tokens_held, token_bank)
        print(f'End of round {current_round}\n')

    final_score = score.get_score(islands, tokens_held)
    print(f"Great game!!! My final score was {final_score}. I hope you had as much fun as I did. I'll be waiting for a "
          f"rematch!")


if __name__ == '__main__':
    print(
        'Welcome to the Emerge AI.\n'
        'My name is Sandy and I will be playing Emerge along with you today. Let us begin!\n'
    )
    game_runner()
