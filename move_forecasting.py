import copy
from scoring import island_score
from typing import Any


#   creates an inverse possibility dictionary the determines how many times a feature is not possible to be played
def move_possibility(move_set):
    #   stores each feature and the amount of times it occurs as not possible for each island
    move_possibilities = {}
    #   iterates over all the features and determines how many 0 values occur for each feature
    for island, features in move_set.items():
        # check if the key is already present in move_possibilities
        for feature, possible in features.items():
            if feature in move_possibilities:
                # increment count if the value is 0
                move_possibilities[feature] += 1 if possible == 0 else 0
            else:
                # initialize count if the key is not present
                move_possibilities[feature] = 1 if possible == 0 else 0

    return move_possibilities


#   takes all possible feature moves and determines the point values associated with them
def weigh_moves(islands):
    move_set = check_moves(islands)
    island_weights = {}
    #   iterates over all islands and their possible feature moves
    for island, possible_moves in move_set.items():
        move_weights = {}
        #   iterates each specific type of feature for all the possible moves in an island
        for feature in possible_moves:
            #   calculates the point value of all possible feature moves
            if possible_moves[feature] == 1:
                next_board = copy.deepcopy(islands[island])
                #   increases the value of the possible move's feature to calculate the score from making that feature
                next_board[feature] += 1
                # TODO make it so placing your first island shows as 1 point, otherwise it will be zero and not occur
                points = island_score(next_board) - island_score(islands[island])
                move_weights[feature] = points
        #   saves the feature weights to its corresponding island
        island_weights[island] = move_weights
    return island_weights


#   sorts the weights into a list of tuples in descending score order
def sort_weights(weights):
    all_weights = []
    for island, features in weights.items():
        for feature, score in features.items():
            all_weights.append((feature, score, island))

    all_weights.sort(key=lambda x: x[1], reverse=True)
    return all_weights


def check_moves(islands):  # Take islands as the input
    #   finds if each feature is able to be played
    move_set = {}
    for island, features in islands.items():
        island_move_set = {
                'Plants': features['Plants'] < 3 and features['Tectonic'] > 0,
                'Crab': features['Plants'] > 0 and features['Crab'] < 1,
                'Turtle': features['Crab'] == 1 and features['Turtle'] < 1,
                'Seal': features['Turtle'] == 1 and features['Seal'] < 1,
                'Tectonic': features['Tectonic'] < 3,
                'Bird': features['Tectonic'] > 0 and features['Bird'] < 1
            }
        move_set[island] = island_move_set
    return move_set

