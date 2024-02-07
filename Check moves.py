def check_moves(game_moves):
    islands = game_moves['islands']
    move_set = {}
    for island, features in islands.items():
        moves = {}
        if features['Tectonic'] > 0:
            moves['Plants'] = get_plant(features)
            moves['Crab'] = get_crab(features)
            moves['Turtle'] = get_turtle(features)
            moves['Seal'] = get_seal(features)
            moves['Tectonic'] = get_tectonic(features)
            moves['Bird'] = get_bird(features)
        else:
            moves = {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0}
        move_set[island] = moves
    print(move_set)

def get_plant(features):
    if features["Plants"] < 3:
        return 1
    else:
        return 0

def get_crab(features):
    if features['Plants'] > 0 and features['Crab'] == 0:
        return 1
    else:
        return 0

def get_turtle(features):
    if features['Crab'] == 1 and features['Turtle'] == 0:
        return 1
    else:
        return 0

def get_seal(features):
    if features['Turtle'] == 1 and features['Seal'] == 0:
        return 1
    else:
        return 0

def get_tectonic(features):
    if features["Tectonic"] < 3:
        return 1
    else:
        return 0

def get_bird(features):
    if features['Bird'] == 0:
        return 1
    else:
        return 0

if __name__ == '__main__':

    print('Welcome to the Emerge AI.\n My name is Sandy and I will be playing Emerge along with you today. Let us begin!')

    game_moves = {
        'modifiers': {1: 'Plant', 2: 'Crab', 3: 'Turtle', 4: 'Seal', 5: 'Island', 6: 'Bird'},
        'islands': {
            '1': {'Plants': 3, 'Crab': 1, 'Turtle': 0, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
            '2': {'Plants': 1, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 3, 'Bird': 0},
            '3': {'Plants': 1, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 0},
            '4': {'Plants': 0, 'Crab': 0, 'Turtle': 0, 'Seal': 0, 'Tectonic': 0, 'Bird': 0},
        },
        'score': 0
    }
    check_moves(game_moves)