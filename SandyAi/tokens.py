class research_token:
    def __init__(self, feature, num, effect, outcome):
        self.feature = feature
        self.num = num
        self.effect = effect
        self.outcome = outcome


#   TODO checks research tokens to see if they are usable for this round
def use_token(tokens, feature: object = None) -> object:
    return None


#   TODO create function that purchases tokens
def buy_tokens(tokens_held, dice):
    if dice >= 2:
        feature = get_feature()
        number = get_num()
    return None

def get_feature():
    '''
    #   TODO docstring
    :return:
    '''
    feature = input('What feature token should I buy?/n(1) Plants/n(2) Crab/n(3) Turtle/n(4) Seal/n(5) Bird/n(6) '
                    'Board').strip()
    if feature == '1':
        return 'Plants'
    elif feature == '2':
        return 'Crab'
    elif feature == '3':
        return 'Turtle'
    elif feature == '4':
        return 'Seal'
    elif feature == '5':
        return 'Bird'
    elif feature == '6':
        return 'Board'
    else:
        print('Invalid response please enter 1, 2, 3, 4, 5, or 6/n')
        get_feature()


def get_num():
    feature = input('What number token should I buy?/n(1) /n(2) /n(3)'
                    'Board').strip()
    if feature == '1':
        return 1
    elif feature == '2':
        return 2
    elif feature == '3':
        return 3


def generate_bank():
    token_bank = []
    token_bank.append(Plants1=research_token('Plants', 1, 'Tectonic', None),
                      Crab1=research_token('Crab', 1, 'cost', 1),
                      Crab2=research_token('Crab', 2, 'cost', None),
                      Crab3=research_token('Crab', 3, 'Tectonic', None),
                      Turtle1=research_token('Turtle', 1, 'cost', 2),
                      Turtle2=research_token('Turtle', 2, 'Tectonic', None),
                      Turtle3=research_token('Turtle', 3, 'Plants', None),
                      Seal1=research_token('Seal', 1, 'cost', 3),
                      Seal2=research_token('Seal', 2, 'Plants', None),
                      Bird1=research_token('Bird', 1, 'cost', 2),
                      Bird2=research_token('Bird', 2, 'Plants', None),
                      Bird3=research_token('Bird', 3, 'Tectonic', None),
                      Board1=research_token('Board', 1, 'dice', None),
                      Board2=research_token('Board', 2, 'mods', None))
    return token_bank