import copy
from SandyAi import decide as dm, scoring


#   takes all possible feature moves and determines the point values associated with them
def weigh_moves(islands):
    """
    Determines the points that will be gained by taking each of moves currently available.

    :param islands: dict[int, dict[str, int]]
        Contains island numbers and their current feature configuration

    :return: dict[int, dict[str, int]]

    :example:
    >>> islands = {1: {'Plants': 1, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 1}}
    >>> weigh_moves(islands)
    {1: {'Plants': 1, 'Turtle': 1, 'Tectonic': 3}}
    """
    move_set = check_moves(islands)
    island_weights = {}
    empty_island = {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0}
    #   iterates over all islands and their possible feature moves
    for island, possible_moves in move_set.items():
        move_weights = {}
        #   assigns the creation of a new island a value of 1 point
        if islands[island] == empty_island:
            move_weights['Tectonic'] = 1
        else:
            #   iterates each specific type of feature for all the possible moves in an island
            for feature in possible_moves:
                #   calculates the point value of all possible feature moves
                if possible_moves[feature] == 1:
                    next_board = copy.deepcopy(islands)
                    # increases the value of the possible move's feature to calculate the score from making that feature
                    next_board = dm.update_board(feature, island, next_board)[0]
                    points = scoring.get_score(next_board) - scoring.get_score(islands)
                    move_weights[feature] = points
        #   saves the feature weights to its corresponding island
        island_weights[island] = move_weights
    return island_weights


def sum_feature_weights(weights):
    """
    Totals each features' score weight across all islands in the weights dictionary.

    :param weights: dict[int, dict[str, int]
        Contains the island numbers and sub-dictionaries containing the features and corresponding score weight.

    :return: dict[str, int]
        Shows the respective total score weights for each feature across all islands.

    :example:
    >>> weights = {
    >>>     1: {'Plants': 1, 'Crab': 1, 'Tectonic': 1, 'Bird': 2},
    >>>     2: {'Plants': 1, 'Seal': 4, 'Tectonic': 3, 'Bird': 2}
    >>> }
    >>> sum_feature_weights(weights)
    {'Plants': 2, 'Crab': 1, 'Turtle: 0, 'Seal': 4, 'Tectonic': 4, 'Bird': 4}
    """
    feature_totals = {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0}
    for island, features in weights.items():
        for feature, weight in features.items():
            feature_totals[feature] += weight
    return feature_totals


#   sorts the weights into a list of tuples in descending score order
def sort_weights(weights):
    """
    Creates a tuple for each unique feature, island combination and its corresponding score weight,
    and sorts it into descending order by weight.

    :param weights: dict[int, dict[str, int]]
        Contains the island numbers and sub-dictionary of each islands' features' score weight.

    :return: list[tuple(str, int, int)]
        A list containing tuples that represent each unique feature, island configuration and its corresponding
        score weight.

    :example:
    """
    all_weights = []
    for island, features in weights.items():
        for feature, score in features.items():
            all_weights.append((feature, score, island))
    #   TODO does this violate the SRP?
    all_weights.sort(key=lambda x: x[1], reverse=True)
    return all_weights


def check_moves(islands):  # Take islands as the input
    """
    Checks each feature on each island to see if it would be playable in the next round

    :param islands: dict[int, dict[str, int]]
        Contains island numbers and their current feature configuration

    :return: dict[int, dict[str, bool]
        Dictionary containing the island numbers and sub-dictionaries containing the feature and a bool that indicates
        if the feature is playable or not.

    :example:
    >>> islands = {1: {'Plants': 2, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 1}}
    >>> check_moves(islands)
    {1: {'Plants': True, 'Crab': False, 'Turtle': True, 'Seal': False, 'Tectonic': True, 'Bird': False}}
    """
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
