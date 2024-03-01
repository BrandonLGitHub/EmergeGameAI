from dice_functions import dice_budget
from move_forecasting import weigh_moves, check_moves
from modifier_functions import flatten, sort_dict


#   Makes turn decisions based off available moves
def spend_dice(islands, modifiers, dice, land_birds, tokens):
    weights = weigh_moves(islands)
    sorted_weights = sort_dict(flatten(weights))
    budget = dice_budget(modifiers, dice['dice_result'], dice['dice_amt'])
    move_set = check_moves(islands)
    ''' TODO create a loop that finds the highest weight in the weights dictionary, checks if it can be afforded, if it can
        buy it, if it cant move on to the next highest move until the dice budget cannot afford anymore moves. 
        After that use buy tokens or save dice to store dice or get a research token if there are any dice remaining'''

    return islands, land_birds


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
