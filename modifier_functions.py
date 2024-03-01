import copy
import move_forecasting as forecast


#   sets the modifiers to the feature that will give you the highest point value
def set_modifiers(modifiers, islands):  # can this be broken into other functions
    current_modifiers = copy.deepcopy(modifiers)
    default_modifiers = {'Plants': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]}
    new_modifiers = copy.deepcopy(default_modifiers)

    weights = forecast.weigh_moves(islands)
    move_set = forecast.check_moves(islands)
    move_possibilities = forecast.move_possibility(move_set)
    replace_modifiers = extract_two_highest_values(move_possibilities)
    all_weights = flatten(weights)
    chosen_modifiers = extract_two_highest_values(all_weights)

    for feature, replace_feature in zip(chosen_modifiers, replace_modifiers):  # look into enumerate for this function
        if len(current_modifiers[feature]) < 2:
            dice_number = default_modifiers[replace_feature][0]
            new_modifiers[replace_feature] = []
            new_modifiers[feature].append(dice_number)
    return current_modifiers


#   takes a sorted dictionary and extracts the two highest values
def extract_two_highest_values(dictionary):
    sorted_dict = sort_dict(dictionary)
    highest_two_values = [value[0] for value in sorted_dict]
    return highest_two_values


#   sorts a dictionary by descending values
def sort_dict(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict


#   flattens a dictionary that contains sub dictionaries
def flatten(dictionary):
    flattened = {key: value for sub_dict in dictionary.values() for key, value in sub_dict.items()}
    return flattened
