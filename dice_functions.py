import random


#   takes the dice roll and totals up the amount of each feature's associated number(s) from the dice in hand
#   TODO consider making this a class
def dice_budget(modifiers, dice_hand, dice_amt):  # modify this to take the modifiers directly as an input
    """
    Totals the amount of dice in the dice hand that can go towards purchasing each feature.

    :param modifiers: dict[str, list[int]]
        Contains the features and their associated value that can be used for purchase.
    :param dice_hand: list[int]
        The values obtained from rolling the dice.
    :param dice_amt: int
        The amount of dice rolled.

    :return: dict[str, int]
        Represents the total number of dice that match to each features' value(s).

    :example:

    >>> modifiers = {'Plants': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]}
    >>> dice_hand = [1, 1, 2, 4, 5, 6, 6]
    >>> dice_amt = 7
    >>> dice_budget(modifiers, dice_hand, dice_amt)
    {'Plants': 2, 'Crab': 1, 'Turtle': 0, 'Seal': 1, 'Tectonic': 1, 'Bird': 2, 'dice_remaining': 7, 'dice_hand': [1,1,2,4,5,6,6]}
    """
    budget = {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0,
              'dice_remaining': dice_amt, 'dice_hand': dice_hand}
    #   looks at each feature and the number value that can be used to purchase board items
    for feature, values in modifiers.items():
        for number in dice_hand:
            #   checks if the number rolled is a number associated with a feature
            if number in values:
                budget[feature] += 1
    return budget


#   rolls the dice available minus the amount of dice saved from the previous turn
def roll_dice(dice_amt, saved_dice):
    """
    Simulates rolling of a certain amount of 6 sided dice.
    :param dice_amt: int
        The amount of dice that are available to be rolled prior to deducting the amount of dice saved from prior round.
    :param saved_dice: list[int]
        The dice values saved from prior round.

    :return: list[int]
        The dice to be used in the next round of moves. Includes any saved dice values and new generated values that
        total up to the dice_amt.

    :example:
    >>> dice_amt = 6
    >>> saved_dice = [2,3]
    >>> roll_dice(dice_amt, saved_dice)
    [*,*,*,*,2,3]
    * representing any number between 1 & 6.
    """
    # Generates rolls for the dice
    rollable_dice = dice_amt - len(saved_dice)
    dice_rolled: list[int] = [random.randint(1, 6) for x in range(rollable_dice)]
    # adds saved dice back into the dice hand
    dice_rolled.extend(saved_dice)
    return dice_rolled


#   sets dice number to correct amount dependent upon round number. 1 Dice is added on every even round
def dice_count(round_num):
    """
    Sets the amount of dice able to be used based of the current round of the game.

    :param round_num: int
        Current round of the game.

    :return: int
        Amount of dice that can be used for his round.

    :example:
    >>> round_num = 5
    >>> dice_count(round_num)
    8
    """
    # stores the correct dice amount for each round
    dice_per_round = {1: 6, 2: 7, 3: 7, 4: 8, 5: 8, 6: 9, 7: 9, 8: 10}
    return dice_per_round.get(round_num)
