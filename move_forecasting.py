import copy
from scoring import island_score
from typing import Any


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
                next_board = copy.deepcopy(islands[island])
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

