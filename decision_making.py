from dice_functions import dice_budget
import move_forecasting as forecast
import copy
import tokens


#   Makes turn decisions based off available feature moves
def spend_dice(islands, modifiers, dice, land_birds, tokens_held):
    """
    Purchases the features with the greatest point values that are afforable using the dice rolled

    :param islands: dict[int, dict[str, int]]
        Contains all the islands and their corresponding configurations.
    :param modifiers: dict[int, list[int]]
        The features and their corresponding modifier values.
    :param dice: dict[str, list[Any] | int | Any]
        Contains the dice remaining, int, the dice hand, list[], and saved dice, list[].
    :param land_birds: int
        Represents the number of birds on the mainland.
    :param tokens_held: #TODO add tokens_held
        Dictionary containing the tokens owned.

    :return: tuple(dict[str, dict[str, int]], int, list[int], #TODO add tokens
        Contains the updates islands, land_birds, saved dice, and token values

    :example:

    >>> islands = {
    >>>             1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
    >>>             2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
    >>>             3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
    >>>             4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
    >>>     }
    >>> modifiers = {'Plants': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]}
    >>> dice = {
    >>>         'dice_amt': 6,
    >>>         'roll_result': [1,1,2,1,3,4],
    >>>         'saved_dice': []
    >>>      }
    >>> land_birds = 2
    >>> tokens_held = None
    >>> spend_dice(islands, modifiers, dice, land_birds, tokens_held)
    #   TODO add result
    """
    #   determines the point values of every possible move
    weights = forecast.weigh_moves(islands)
    #   sorts the weights in descending order and returns a list of tuples with the corresponding feature and island
    sorted_weights = forecast.sort_weights(weights)
    budget = dice_budget(modifiers, dice['roll_result'], dice['dice_amt'])
    for feature, score, island in sorted_weights:
        cost = check_cost(feature, island, islands, land_birds, tokens_held)
        if affordability(feature, cost, budget):
            islands, land_birds, tokens_held = update_board(feature, island, islands, land_birds, tokens_held)
            budget = update_budget(feature, cost, budget, modifiers)
    #   TODO buy_tokens()
    tokens_held = tokens.buy_tokens(dice)
    #   TODO save_dice()
    saved_dice = save_dice(weights, dice)
    return islands, land_birds, saved_dice, tokens_held


#   checks the budget to see if a feature can be purchased
def affordability(feature, cost, budget):
    """
    Checks if a feature's budget and the amount of dice remaining can afford the cost of a feature.

    :param feature: str
        The feature that will be checked for affordability
    :param cost: int
        The cost of updating the desired feature
    :param budget:dict[str, Union[int, list]]
        A dictionary representing the budget, where keys are strings indicating items,
        and values are either integers representing feature budgets and the dice remaining or lists representing
        the dice hand.

    :return: bool

    :example:

    >>> feature = 'Seal'
    >>> cost = 4
    >>> budget = {'Plants': 2, 'Crab': 1, 'Turtle': 0, 'Seal': 4, 'Tectonic': 0, 'Bird': 0,
    >>>             'dice_remaining': 7, 'dice_hand': [1,1,2,4,4,4,4]}
    >>> affordability(feature, cost, budget)
    True
    """
    if budget[feature] >= cost and budget['dice_remaining'] >= cost:
        return True
    else:
        return False


#   updates the board based off the feature move made
#   TODO Test this function for island input
def update_board(feature, island, islands, land_birds_count=0, tokens_held=None):
    """
    Update the board by selecting the specified island from the islands and incrementing the
    specified feature by 1

    :param feature: str
        The feature being updated
    :param island: int
        The island whose feature is being updated
    :param islands: dict[int, dict[str, int]]
        Dictionary containing all the islands
    :param land_birds_count: int
        Count of the birds on the mainland of the board
    :param tokens_held: dict
        Contains current toke information

    :return: tuple(dict[str, dict[str, int]], int)
        The updated islands and the updated count of land_birds

    :example:

    >>> feature = 'Crab'
    >>> island = 2
    >>> islands = {
    >>>    1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
    >>>    2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
    >>>    3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
    >>>    4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
    >>> }
    >>> land_birds_count = 2
    >>> tokens_held = None
    >>> update_board(feature,island,islands,land_birds_count,tokens_held)
    {
        1: {'Plants': 1, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
        2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
        3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
        4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
     }
    """
    if island in islands:
        islands[island][feature] += 1
        if feature == 'Bird':
            if land_birds_count > 0:
                land_birds_count -= 1
            if islands[island]['Plants'] < 4:
                islands[island]['Plants'] += 1
        if feature == 'Tectonic' and islands[island]['Tectonic'] == 0:
            tokens_held = tokens.buy_tokens(0)  # TODO once token system is working

    return islands, land_birds_count, tokens_held


#   updates the budget based of the cost of a feature
def update_budget(feature, cost, budget, modifiers):
    """
    Update the budget based on the given feature and modifiers.

    :param feature: str
        The feature to be updated
    :param cost: int
        The cost associated with the feature, determining the amount subtracted from the feature's budget, dice remaining
        and modifications made to the dice hand.
    :param budget: dict[str, Union[int, list]]
        A dictionary representing the budget, where keys are strings indicating items,
        and values are either integers representing feature budgets and the dice remaining or lists representing
        the dice hand.
    :param modifiers: dict[str, list[int]]
        A dictionary containing the modifiers associated with each feature.

    :return: dict[str, Union[int, list]]
        The updated budget after subtracting the cost and updating the dice hand

    :example:

    >>> Feature = "Plants"
    >>> cost = 2
    >>> budget = {'Plants': 2, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0,
    >>>             'dice_remaining': 6, 'dice_hand': [1,1,2,3,5,6]}
    >>> modifiers = {'Plants': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]}
    >>> update_budget(feature,cost,budget,modifiers)
    {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0,
    'dice_remaining': 4, 'dice_hand': [2,3,5,6]}
    """
    budget[feature] -= cost
    budget['dice_remaining'] -= cost
    budget['dice_hand'] = update_dicehand(feature, cost, budget['dice_hand'], modifiers)
    return budget


#   updates the dice hand based off the dice spent from the hand
def update_dicehand(feature, cost, hand, modifiers):
    """
    Update the dice hand based on the given feature and modifiers.

    :param feature: str
        The feature to be updated.
    :param cost: int
        The cost associated with the feature, determining the number of modifications allowed.
    :param hand: list[int]
        The list representing the current dice hand.
    :param modifiers: dict[str, list[int]]
        A dictionary containing the modifiers associated with each feature.

    :return: list[int]
        The updated dice hand after subtracting the cost for the approrpiate feature's corresponding modifiers.

    :example:

    >>> hand = [1, 2, 3, 4, 5]
    >>> feature = "remove"
    >>> cost = 2
    >>> modifiers = {"remove": [2, 4]}
    >>> update_dicehand(feature,cost,hand,modifiers)
    [1, 3, 5]
    """
    count = 0
    hand_copy = copy.copy(hand)
    for num in hand:
        if num in modifiers[feature]:
            hand_copy.remove(num)
            count += 1
            if count == cost:
                break
    return hand_copy


#   checks the islands and research tokens to determine the cost of a feature
def check_cost(feature, island, islands, land_birds, tokens_held):
    """
    Returns the cost of updating a given feature based off the chosen island's configuration, any research token
    discounts, and for the Bird feature, checks to see if there are birds on the mainland.

    :param feature: str
        The feature for which the cost is being determined.
    :param island: int
        The island that is being checked for cost
    :param islands: dict[int, dict[str, int]]
        Dictionary containing all the islands' configurations
    :param land_birds: int
        Represents the birds remaining on the mainland which can be purchased at a lower cost.
    :param tokens_held:# TODO create tokens type


    :return: int
        The cost of upgrading the chosen feature on the chosen island

    :example:

    >>> feature = 'Bird'
    >>> island = 1
    >>> islands = {
    >>>                  1: {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
    >>>                  2: {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
    >>>                  3: {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 2, 'Bird': 0},
    >>>                  4: {'Plants': 2, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 1},
    >>>                }
    >>> land_birds = 2
    >>> tokens_held = None
    >>> check_cost(feature, island, islands, land_birds, tokens_held)
    2

    """
    #   checks to see if there is a research token that would change the price
    cost = tokens.use_token(tokens_held, feature)
    #   dictionary establishing the price of features that do no change based off board status
    fxd_prices = {'Crab': 2, 'Turtle': 3, 'Seal': 4}
    #   checks the price if there was no token applicable
    if cost is None:
        #   determines the price of plants based off the amount on the island
        if feature == 'Plants':
            plant_prices = {0: 1, 1: 2, 2: 3}
            total = islands[island]['Plants']
            cost = plant_prices[total]
        #   determines the price of a tectonic upgrade based off the island's current size
        elif feature == 'Tectonic':
            tec_prices = {0: 2, 1: 3, 2: 4}
            total = islands[island]['Tectonic']
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


#   TODO create function that saves any dice that contribute to the highest weighted feature move
def save_dice(weights, dice):
    return None
