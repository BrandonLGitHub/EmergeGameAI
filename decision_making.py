#   import dice budget
import copy


#   import island score


#   this function looks for the move that would give them the most points in the next round
#   and sets a modifier for that move over the move that is the least likely to occur
#   !!! NEED TO SOLVE WHAT TO DO IF THE LEAST LIKELY MOVE ALSO IS ONE OF THE HIGHEST POINT VALUES !!!
def set_modifiers(current_board):  # can this be broken into other functions
    current_modifiers = copy.copy(current_board['modifiers'])
    #   default modifiers set to be changed to represent the next modifier configuration
    default_modifiers = {'Plants': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]}
    new_modifiers = copy.copy(default_modifiers)
    weights = weigh_moves(current_board)
    move_set = check_moves(current_board['islands'])
    #   stores each move and the amount of times it occurs as not possible for each island
    move_possibilities = move_possibility(move_set)

    #   finds the two moves that are the least likely to be playable and their corresponding keys
    unlikely_moves = sorted(move_possibilities.items(), key=lambda x: x[1], reverse=True)
    replace_modifiers = list(dict(unlikely_moves[:2]).keys())

    #   flatten the sub-dictionaries into a single dictionary
    all_weights = {}
    for island in weights.values():
        all_weights.update(island)

    # find the two highest weights and their corresponding keys
    sorted_weights = sorted(all_weights.items(), key=lambda x: x[1], reverse=True)
    chosen_modifiers = list(dict(sorted_weights[:2]).keys())

    count = -1
    for feature in chosen_modifiers:  # look into enumerate for this function
        count += 1
        if len(current_modifiers[feature]) < 2:
            dice_number = default_modifiers[replace_modifiers[count]]
            dice_number = dice_number[0]
            print(dice_number)
            new_modifiers[replace_modifiers[count]] = []
            new_modifiers[feature].append(dice_number)
    return current_modifiers


#   Makes turn decisions based off available moves
def spend_dice(
        current_board):  # change this to take the weights and budget as variables rather than running the program on their own
    weights = weigh_moves(current_board)
    budget = dice_budget(current_board)
    return current_board['islands']


#   checks the islands and research tokens to determine the cost of a feature
def check_cost(feature, island,
               current_board):  # change this to take the token use and islands as variables rather than running the program on their own
    #   checks to see if there is a research token that would change the price
    cost = use_token(current_board, feature)
    #   dictionary establishing the price of features that do no change based off board status
    fxd_prices = {'Crab': 2, 'Turtle': 3, 'Seal': 4}
    #   checks the price if there was no token applicable
    if cost is None:
        #   determines the price of plants based off the amount on the island
        if feature == 'Plants':
            plant_prices = {0: 1, 1: 2, 2: 3}
            total = current_board['islands'][island]['Plants']
            cost = plant_prices[total]
        #   determines the price of a tectonic upgrade based off the island's current size
        elif feature == 'Tectonic':
            tec_prices = {0: 2, 1: 3, 2: 4}
            total = current_board['islands'][island]['Tectonic']
            cost = tec_prices[total]
        #   checks to see if there are bird on the mainland to determine the price
        elif feature == 'Bird':
            if current_board['land_birds'] > 0:
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
def weigh_moves(current_board):
    move_set = check_moves(current_board['islands'])
    island_weights = {}
    #   iterates over all islands and their ossible moves
    for island, possible_moves in move_set.items():
        move_weights = {}
        #   iterates each specific type of move for all the possible moves in an island
        for move in possible_moves:
            #   calculates the point value of all possible moves
            if possible_moves[move] == 1:
                next_board = copy.copy(current_board['islands'][island])
                #   increases the value of the possible move's feature to calculate the score from making that move
                next_board[move] += 1
                points = island_score(next_board) - island_score(current_board['islands'][island])
                move_weights[move] = points
        #   saves the move weights to its corresponding island
        island_weights[island] = move_weights
    return island_weights


def check_moves(islands):  # Take islands as the input
    #   finds if each feature is able to be played
    for island, features in islands.items():
        move_set = {
            'Plants': features['Plants'] < 3 and features['Tectonic'] > 0,
            'Crab': features['Plants'] > 0 and features['Crab'] < 1,
            'Turtle': features['Crab'] == 1 and features['Turtle'] < 1,
            'Seal': features['Turtle'] == 1 and features['Seal'] < 1,
            'Tectonic': features['Tectonic'] < 3,
            'Bird': features['Tectonic'] > 0 and features['Bird'] < 1
        }
    return move_set
