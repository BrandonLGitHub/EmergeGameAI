from typing import Any


# calculates the total score of the board
def get_score(islands):
    """
    Calculates the score of all islands.

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
    for island in islands:
        score += island_score(island)
    return score


# calculates the score of individual islands
def island_score(island):
    """
    Checks the score of an individual island.

    :param island: dict[str, int]
        Represents which features and how many of each is present on the island.

    :return: int
        Score of the island.

    :example:

    >>> island = {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0}
    >>> island_score(island)
    8
    """
    inhabitants = ['Plants', 'Crab', 'Turtle', 'Seal', 'Bird']
    #   calculate total amount of inhabitants on an island
    total_inhabitants = sum(island[key] for key in inhabitants)
    #   calculates the score by multiplying the total inhabitants by the level of tectonics
    score: int | Any = total_inhabitants * island['Tectonic']
    #   add bonus points for having all animals except birds on your island
    if island['Seal'] == 1:
        score += 3

    return score
