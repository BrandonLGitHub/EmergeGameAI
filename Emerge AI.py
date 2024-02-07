import random
import copy


def game_runner():
    current_board = {
        #   initial modifier set up
        'modifiers': {'Plant': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]},
        #   initial island settings
        'islands': {
            1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
            2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
            3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
            4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
        },
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
        current_board = game_play(current_board)
        print(f'End of round {current_board["round"]}')


#   STAGE1
#   this function looks for the move that would give them the most points in the next round
#   and sets a modifier for that move over the move that is the least likely to occur
#   !!! NEED TO SOLVE WHAT TO DO IF THE LEAST LIKELY MOVE ALSO IS ONE OF THE HIGHEST POINT VALUES !!!
def set_modifiers(current_board):
    current_modifiers = copy.copy(current_board['modifiers'])
    #   default modifiers set to be changed to represent the next modifier configuration
    default_modifiers = {'Plant': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]}
    new_modifiers = copy.copy(default_modifiers)
    weights = weigh_moves(current_board)
    move_set = check_moves(current_board)
    #   stores each move and the amount of times it occurs as not possible for each island
    move_possibilities = move_possibility(move_set)

    #   finds the move that is the least likely and most likely to be playable and their corresponding keys
    unlikely_moves = sorted(move_possibilities.items(), key=lambda x: x[1], reverse=True)
    replace_modifiers = list(dict(unlikely_moves[:2]).keys())

    #   flatten the sub-dictionaries into a single dictionary
    all_weights = {}
    for island in weights.values():
        all_weights.update(island)

    # find the two highest weights and their corresponding keys
    sorted_weights = sorted(all_weights.items(), key=lambda x: x[1], reverse=True)
    chosen_modifiers = list(dict(sorted_weights[:2]).keys())
    print(f'Chosen modifiers: {chosen_modifiers}\nReplacement modifiers: {replace_modifiers}')

    count = -1
    for feature in chosen_modifiers:
        count += 1
        print(current_modifiers[feature])
        if len(current_modifiers[feature]) < 2:
            dice_number = default_modifiers[replace_modifiers[count]]
            dice_number = dice_number[0]
            print(dice_number)
            new_modifiers[replace_modifiers[count]] = []
            new_modifiers[feature].append(dice_number)
    print(f'The new modifiers are {new_modifiers}')
    return current_modifiers


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


#   STAGE2
#   rolls the dice available minus the amount of dice saved from the previous turn
def roll_dice(dice_amt, saved_dice):
    # saves the values of the dice rolled by the computer
    dice_rolled = []
    # rolls the dice available for a roll
    for x in range(dice_amt):
        roll = random.randint(1, 6)
        dice_rolled.append(roll)
    # adds saved dice back into the dice hand
    for d in saved_dice:
        dice_rolled.append(d)
    return dice_rolled


#   sets dice number to correct amount dependent upon round number. 1 Dice is added on every even round
def dice_count(round_num):
    # stores the correct dice amount for each round
    dice_per_round = {1: 6, 2: 7, 3: 7, 4: 8, 5: 8, 6: 9, 7: 9, 8: 10}
    dice_num = dice_per_round.get(round_num)
    return dice_num


#   STAGE3
#   Makes turn decisions based off available moves
def game_play(current_board):
    weights = weigh_moves(current_board)
    return current_board


#   takes the dice roll and totals up the amount of each feature can be purchased from the dice in hand
def dice_budget(current_board):
    modifiers = current_board['modifiers']
    dice_hand = current_board['roll_result']
    return budget


#   takes all possible moves and determines the point values associated with them
def weigh_moves(current_board):
    move_set = check_moves(current_board)
    island_weights = {}
    #   iterates over all islands and their possible moves
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


#   takes the pieces currently on the board and determines what moves can be made.
def check_moves(current_board):
    islands = current_board['islands']
    move_set = {}
    #   finds if each feature is able to be played
    for island, features in islands.items():
        move_set[island] = {'Plants': get_plant(features), 'Crab': get_crab(features),
                            'Turtle': get_turtle(features), 'Seal': get_seal(features),
                            'Tectonic': get_tectonic(features),
                            'Bird': get_bird(features)}
    return move_set


#   these functions check their respective features for the possibility of being played
def get_plant(features):
    if features["Plants"] < 3 and features['Tectonic'] > 0:
        return 1
    else:
        return 0


def get_crab(features):
    if features['Plants'] > 0 and features['Crab'] < 1:
        return 1
    else:
        return 0


def get_turtle(features):
    if features['Crab'] == 1 and features['Turtle'] < 1:
        return 1
    else:
        return 0


def get_seal(features):
    if features['Turtle'] == 1 and features['Seal'] < 1:
        return 1
    else:
        return 0


def get_tectonic(features):
    if features["Tectonic"] < 3:
        return 1
    else:
        return 0


def get_bird(features):
    if features['Bird'] == 0 and features['Tectonic'] > 0:
        return 1
    else:
        return 0


# calculates the total score of the board
def get_score(current_board):
    islands = current_board['islands']
    score = 0
    for island in islands:
        score += island_score(island)
    return score


# calculates the score of individual islands
def island_score(island):
    score = 0
    inhabitants = ['Plants', 'Crab', 'Turtle', 'Seal', 'Bird']
    #   sums all the inhabitants on the island and then multiplies by the level of tectonics
    score += (sum(island[key] for key in inhabitants) * island['Tectonic'])
    #   includes the "biodiversity" point bonus for having all animals except birds on your island
    if island['Seal'] == 1:
        score += 3
    return score


if __name__ == '__main__':
    print(
        'Welcome to the Emerge AI.\n'
        'My name is Sandy and I will be playing Emerge along with you today. Let us begin!\n'
    )
    game_runner()
