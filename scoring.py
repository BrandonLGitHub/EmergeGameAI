from typing import Any


# calculates the total score of the board
def get_score(islands):  #take islands as an import
    score = 0
    for island in islands:
        score += island_score(island)
    return score


# calculates the score of individual islands
def island_score(island):
    inhabitants = ['Plants', 'Crab', 'Turtle', 'Seal', 'Bird']
    #   calculate total amount of inhabitants on an island
    total_inhabitants = sum(island[key] for key in inhabitants)
    #   calculates the score by multiplying the total inhabitants by the level of tectonics
    score: int | Any = total_inhabitants * island['Tectonic']
    #   add bonus points for having all animals except birds on your island
    if island['Seal'] == 1:
        score += 3

    return score
