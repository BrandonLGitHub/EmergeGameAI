
# calculates the total score of the board
def get_score(islands):  #take islands as an import
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
