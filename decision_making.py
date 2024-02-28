import copy
from dice_functions import dice_budget
from scoring import island_score
from typing import List, Dict, Any


#   sets the modifiers to the feature that will give you the highest point value
def set_modifiers(modifiers, islands):  # can this be broken into other functions
    current_modifiers = copy.deepcopy(modifiers)
    default_modifiers = {'Plants': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]}
    new_modifiers = copy.deepcopy(default_modifiers)

    weights = weigh_moves(islands)
    move_set = check_moves(islands)
    move_possibilities = move_possibility(move_set)
    replace_modifiers = extract_two_highest_values(move_possibilities)
    all_weights = flatten(weights)
    chosen_modifiers = extract_two_highest_values(all_weights)

    for feature, replace_feature in zip(chosen_modifiers, replace_modifiers):  # look into enumerate for this function
        if len(current_modifiers[feature]) < 2:
            dice_number = default_modifiers[replace_feature][0]
            new_modifiers[replace_feature] = []
            new_modifiers[feature].append(dice_number)
    return current_modifiers


#   takes a sorted dictionary and extracts the two highest values
def extract_two_highest_values(dictionary):
    sorted_dict = sort_dict(dictionary)
    highest_two_values = [value[0] for value in sorted_dict]
    return highest_two_values


#   sorts a dictionary by descending values
def sort_dict(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict


#   flattens a dictionary that contains sub dictionaries
def flatten(dictionary):
    flattened = {key: value for sub_dict in dictionary.values() for key, value in sub_dict.items()}
    return flattened


#   Makes turn decisions based off available moves
def spend_dice(islands, modifiers, dice, land_birds):  # change this to take the weights and budget as variables rather than running the program on their own
    weights = weigh_moves(islands)
    budget = dice_budget(modifiers, dice['dice_result'], dice['dice_amt'])
    return islands, land_birds


#   checks the islands and research tokens to determine the cost of a feature
def check_cost(feature, island,
               land_birds):  # change this to take the token use and islands as variables rather than running the program on their own
    #   checks to see if there is a research token that would change the price
    cost = use_token(current_board, feature)
    #   dictionary establishing the price of features that do no change based off board status
    fxd_prices = {'Crab': 2, 'Turtle': 3, 'Seal': 4}
    #   checks the price if there was no token applicable
    if cost is None:
        #   determines the price of plants based off the amount on the island
        if feature == 'Plants':
            plant_prices = {0: 1, 1: 2, 2: 3}
            total = island['Plants']
            cost = plant_prices[total]
        #   determines the price of a tectonic upgrade based off the island's current size
        elif feature == 'Tectonic':
            tec_prices = {0: 2, 1: 3, 2: 4}
            total = island['Tectonic']
            cost = tec_prices[total]
        #   checks to see if there are bird on the mainland to determine the price
        elif feature == 'Bird':
            if land_birds > 0:
                cost = 2
            else:
                cost = 3
        #   if the feature is not a variable priced feature, selects the feature and its price from the dictionary
        else:
            cost = fxd_prices[feature]
    return cost


#   checks research tokens to see if they are usable for this round
def use_token(current_board: object, feature: object = None) -> object:
    return None


#   creates an inverse possibility dictionary the determines how many times a move is not possible to be played
def move_possibility(move_set):
    #   stores each move and the amount of times it occurs as not possible for each island
    move_possibilities = {}
    #   iterates over all the moves and determines how many 0 values occur for each move
    for island, moves in move_set.items():
        # check if the key is already present in move_possibilities
        for move, possible in moves.items():
            if move in move_possibilities:
                # increment count if the value is 0
                move_possibilities[move] += 1 if possible == 0 else 0
            else:
                # initialize count if the key is not present
                move_possibilities[move] = 1 if possible == 0 else 0

    return move_possibilities


#   takes all possible moves and determines the point values associated with them
def weigh_moves(islands):
    move_set = check_moves(islands)
    island_weights = {}
    #   iterates over all islands and their possible moves
    for island, possible_moves in move_set.items():
        move_weights = {}
        #   iterates each specific type of move for all the possible moves in an island
        for move in possible_moves:
            #   calculates the point value of all possible moves
            if possible_moves[move] == 1:
                next_board = copy.copy(islands[island])
                #   increases the value of the possible move's feature to calculate the score from making that move
                next_board[move] += 1
                points = island_score(next_board) - island_score(islands[island])
                move_weights[move] = points
        #   saves the move weights to its corresponding island
        island_weights[island] = move_weights
    return island_weights


def check_moves(islands):  # Take islands as the input
    #   finds if each feature is able to be played
    for island, features in islands.items():
        move_set: dict[str, bool | Any] = {
            'Plants': features['Plants'] < 3 and features['Tectonic'] > 0,
            'Crab': features['Plants'] > 0 and features['Crab'] < 1,
            'Turtle': features['Crab'] == 1 and features['Turtle'] < 1,
            'Seal': features['Turtle'] == 1 and features['Seal'] < 1,
            'Tectonic': features['Tectonic'] < 3,
            'Bird': features['Tectonic'] > 0 and features['Bird'] < 1
        }
    return move_set
