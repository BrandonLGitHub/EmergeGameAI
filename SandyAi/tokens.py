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
    return None


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
