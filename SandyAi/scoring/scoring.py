from typing import Any


# calculates the total score of the board
def get_score(islands, tokens_held):
    """
    Calculates the score of all islands.

    :param tokens_held:
    :param islands: dict[int: dict[str: int]]
        dictionary containing all the island configurations.

    :return: int
        score of the islands.

    :example:

    >>> islands = {
    >>>    1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
    >>>    2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
    >>>    3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
    >>>    4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
    >>> }
    >>> get_score(islands)
    14
    """
    score = 0
    for island, features in islands.items():
        score += island_score(features)
    score += len(tokens_held)
    return score


# calculates the score of individual islands
def island_score(features):
    """
    Checks the score of an individual island.

    :param features: dict[str, int]
        Represents which features and how many of each is present on the island.

    :return: int
        Score of the island.

    :example:

    >>> features = {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0}
    >>> island_score(features)
    8
    """
    inhabitants = ['Plants', 'Crab', 'Turtle', 'Seal', 'Bird']
    #   calculate total amount of inhabitants on an island
    total_inhabitants = sum(features[key] for key in inhabitants)
    #   calculates the score by multiplying the total inhabitants by the level of tectonics
    score: int | Any = total_inhabitants * features['Tectonic']
    #   add bonus points for having all animals except birds on your island
    if features['Seal'] == 1:
        score += 3

    return score
