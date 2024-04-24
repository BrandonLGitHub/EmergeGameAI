"""Contains functionality related to using research tokens in the game."""


class research_token:
    """
    Represents and contains all the relevant information of a research token, a game pieced used during play.
    """
    def __init__(self, feature, num, effect, outcome, description):
        self.feature = feature
        self.num = num
        self.effect = effect
        self.outcome = outcome
        self.description = description


#   TODO checks research tokens to see if they are usable for this round
def use_token(tokens_held, feature: object = None, use: object = 'other'):
    """
    Takes in the tokens held and the optional feature and use for the token and then uses the appropriate toke if held
    :param tokens_held: list
        Contains all the unused research tokens purchased during the game
    :param feature: str
        Optional feature of the token that is to be used
    :param use: str
        Optional use for the token
    :return:
    """
    #   TODO add functionality for non-cost tokens
    if use == 'other':
        return None, tokens_held
    elif use == 'cost':
        cost, tokens_held = use_token_for_cost(tokens_held, feature)
        return cost, tokens_held
    else:
        return None, tokens_held


def use_token_for_cost(tokens_held, feature):
    """
    Looks for tokens for a specific feature and extracts the discounted cost for that feature if there is one.
    :param tokens_held:
    :param feature:
    :return:
    """
    for token in tokens_held:
        if token.feature == feature and token.effect == 'cost':
            tokens_held.remove(token)
            return token.outcome, tokens_held
    return None, tokens_held


def buy_tokens(tokens_held, dice_count, token_bank):
    """
    Purchases a token(s) based of dice amount and the token selected
    :param tokens_held:
    :param dice_count:
    :param token_bank:
    :return:
    """
    while dice_count >= 2:
        feature = get_feature()
        number = get_num(feature, token_bank)
        bought_token = extract_token(token_bank, feature, number)
        tokens_held.append(bought_token)
        dice_count -= 2
    print('Less than two tokens remaining. Cannot purchase tokens\n')
    return tokens_held


def extract_token(token_bank, chosen_feature, chosen_num):
    """
    Returns the selected research token from the token bank
    :param token_bank: list
        Contains all the types of research tokens
    :param chosen_feature: str
        The feature of the desired research token
    :param chosen_num:
        Number of the specific research token
    :return:
    """
    for token in token_bank:
        if token.feature == chosen_feature and token.num == chosen_num:
            return token
    return None


def get_feature():
    """
    Gets an input from the player of what token feature they want to buy for Sandy
    :return: str
        Chosen feature of the token
    """
    feature = input('What feature token should I buy?\n(1) Plants\n(2) Crab\n(3) Turtle\n(4) Seal\n(5) Tectonic\n(6) '
                    'Bird\n(7) Board\n').strip()
    if feature == '1':
        return 'Plants'
    elif feature == '2':
        return 'Crab'
    elif feature == '3':
        return 'Turtle'
    elif feature == '4':
        return 'Seal'
    elif feature == '5':
        return 'Tectonic'
    elif feature == '6':
        return 'Bird'
    elif feature == '7':
        return 'Board'
    else:
        print('Invalid response please enter 1, 2, 3, 4, 5, or 6\n')
        get_feature()


def get_num(chosen_feature, token_bank):
    """
    Gets input of what number of the token feature they are buying for Sandy
    TODO Docstring
    :param chosen_feature:
    :return: int
    """
    print(f'Which token for the {chosen_feature} feature are we buying?\n')
    #   TODO from the token bank exract all the tokens for the feature and list the numbers and their description
    for token in token_bank:
        if token.feature == chosen_feature:
            print(f'({token.num}): {token.description}')
    number = input().strip()
    if number == '1' and chosen_feature in ('Plants', 'Crab', 'Turtle', 'Seal', 'Bird', 'Board', 'Tectonic'):
        return 1
    elif number == '2' and chosen_feature in ('Crab', 'Turtle', 'Seal', 'Bird', 'Board', 'Tectonic'):
        return 2
    elif number == '3' and chosen_feature in ('Crab', 'Turtle', 'Bird'):
        return 3
    else:
        print('Invalid response please enter one of the available numbers for your feature\n')
        get_num(chosen_feature, token_bank)


def generate_bank():
    """
    Generates a list of all the different research tokens
    :return: list
        Contains all the available research tokens
    """
    plants1 = research_token('Plants', 1, 'Tectonic', None,
                             'When you place a 4th tree on an island, grow that island.')

    crab1 = research_token('Crab', 1, 'cost', 1, 'Place a crab for 1 die.')

    crab2 = research_token('Crab', 2, 'cost', None, 'Place 2 Crabs for 3 dice.')

    crab3 = research_token('Crab', 3, 'Tectonic', None,
                           'When you place 2 Crabs in the same round, grow 1 of the islands.')

    turtle1 = research_token('Turtle', 1, 'cost', 2, 'Place a Turtle for 2 dice.')

    turtle2 = research_token('Turtle', 2, 'Tectonic', None,
                             'When you place a Turtle, grow that island.')

    turtle3 = research_token('Turtle', 3, 'Plants', None,
                             'When you place a Turtle on an island, place 1 Tree on that island')

    seal1 = research_token('Seal', 1, 'cost', 3,'Place 1 Seal for 3 dice.')

    seal2 = research_token('Seal', 2, 'Plants', None,
                           'When you place a Seal, place 1 Tree on that island.')

    bird1 = research_token('Bird', 1, 'cost', 2, 'Steal a Bird for 2 dice.')

    bird2 = research_token('Bird', 2, 'Plants', None,
                           'When you steal a Bird, place 2 Trees on the island it lands on.')

    bird3 = research_token('Bird', 3, 'Tectonic', None,
                           'When you steal a Bird, grown the island it lands on.')

    tectonic1 = research_token('Tectonic', 1, 'cost', 2,
                               'Grow a small island into a medium one for 2 dice.')

    tectonic2 = research_token('Tectonic', 2, 'cost', 3,
                               'Grow a medium island into a large one for 3 dice.')

    board1 = research_token('Board', 1, 'dice', None,
                            'Re-roll any number of dice.')

    board2 = research_token('Board', 2, 'mods', None,
                            'Refresh all your Modifier Tiles')

    token_bank = [plants1, crab1, crab2, crab3, turtle1, turtle2, turtle3, seal1, seal2, tectonic1,
                  tectonic2, bird1, bird2, bird3, board1, board2]
    return token_bank
