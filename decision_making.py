from dice_functions import dice_budget
import move_forecasting as forecast
import copy
from modifier_functions import flatten, sort_dict


#   Makes turn decisions based off available moves
def spend_dice(islands, modifiers, dice, land_birds, tokens):
    weights = forecast.weigh_moves(islands)
    sorted_weights = forecast.sort_weights(weights)
    budget = dice_budget(modifiers, dice['dice_result'], dice['dice_amt'])
    for move, score, island in weights:
        cost = check_cost(move, island, land_birds, tokens)
        if affordability(move, cost, budget):
            islands, land_birds = update_board(move, island, islands, land_birds)
            budget = update_budget(move, cost, budget, modifiers)
    return islands, land_birds, saved_dice, tokens


#   checks the budget to see if a move can be purchased
def affordability(move, cost, budget):
    if budget[move] >= cost:
        return True
    else:
        return False


#   updates the board based off the move made
def update_board(feature, island, islands, land_birds):
    islands[island][feature] += 1
    if feature == 'Bird' and land_birds > 0:
        land_birds -= 1
    return islands, land_birds


#   updates the budget based of the cost of a move
def update_budget(move, cost, budget, modifiers):
    budget[move] -= cost
    budget['dice_remaining'] -= cost
    budget['dice_hand'] = update_dicehand(move, cost, budget['dice_hand'], modifiers)
    return budget


#   updates the dice hand based off the dice spent from the hand
def update_dicehand(move, cost, hand, modifiers):
    count = 0
    hand_copy = copy.copy(hand)
    for num in hand:
        if num in modifiers[move]:
            hand_copy.remove(num)
            count += 1
            if count == cost:
                break
    return hand_copy


#   checks the islands and research tokens to determine the cost of a feature
def check_cost(feature, island, land_birds, tokens):
    #   checks to see if there is a research token that would change the price
    cost = use_token(tokens, feature)
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


#   TODO checks research tokens to see if they are usable for this round
def use_token(tokens, feature: object = None) -> object:
    return None


#   TODO create function that purchases tokens
def buy_tokens(dice):
    return None


#   TODO create function that saves any dice that contribute to the highest weighted move
def save_dice(weights):
    return None
