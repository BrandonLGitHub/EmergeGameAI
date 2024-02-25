import random
import copy


#   takes the dice roll and totals up the amount of each feature can be purchased from the dice in hand
def dice_budget(current_board):  # modify this to take the modifiers directly as an input
    modifiers = current_board['modifiers']
    dice_hand = current_board['roll_result']
    budget = {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0,
              'Dice': current_board['dice_amt']}
    #   goes through all features and its related values
    for feature, values in modifiers.items():
        #   looks at all the numbers from the roll
        for number in dice_hand:
            # checks the roll against all the current number from the roll
            for value in values:
                # if the number and value match, increase that features budget by 1
                if number == value:
                    budget[feature] += 1
    return budget


#   rolls the dice available minus the amount of dice saved from the previous turn
def roll_dice(dice_amt, saved_dice):
    # Generates rolls for the dice
    dice_rolled: list[int] = [random.randint(1, 6) for x in range(dice_amt)]
    # adds saved dice back into the dice hand
    dice_rolled.extend(saved_dice)
    return dice_rolled


#   sets dice number to correct amount dependent upon round number. 1 Dice is added on every even round
def dice_count(round_num):
    # stores the correct dice amount for each round
    dice_per_round = {1: 6, 2: 7, 3: 7, 4: 8, 5: 8, 6: 9, 7: 9, 8: 10}
    assert isinstance(round_num, object)  # what is this for?
    return dice_per_round.get(round_num)
