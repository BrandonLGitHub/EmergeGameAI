import copy
import move_forecasting as forecast


#   sets the modifiers to the feature that will give you the highest point value
def set_modifiers(modifiers, islands):  # can this be broken into other functions
    current_modifiers = copy.deepcopy(modifiers)
    default_modifiers = {'Plants': [1], 'Crab': [2], 'Turtle': [3], 'Seal': [4], 'Tectonic': [5], 'Bird': [6]}
    new_modifiers = copy.deepcopy(default_modifiers)
    #   determines the points gained from making each move
    weights = forecast.weigh_moves(islands)
    #   totals up the weights by feature
    weight_total_per_feature = forecast.sum_feature_weights(weights)
    #   selects the two moves with the lowest point values
    replace_modifiers = extract_two_lowest_values(weight_total_per_feature)
    #   selects the moves with the two highest point value
    chosen_modifiers = extract_two_highest_values(weight_total_per_feature)
    for feature, replace_feature in zip(chosen_modifiers, replace_modifiers):
        if len(current_modifiers[feature]) < 2:
            dice_number = default_modifiers[replace_feature][0]
            new_modifiers[replace_feature] = []
            new_modifiers[feature].append(dice_number)
    return current_modifiers


#   takes a sorted dictionary and extracts the two highest values
def extract_two_highest_values(dictionary):
    sorted_dict = sort_dict_dec(dictionary)
    highest_keys = [item[0] for item in sorted_dict[:2]]
    return highest_keys


def extract_two_lowest_values(dictionary):
    sorted_dict = sort_dict_asc(dictionary)
    lowest_keys = [item[0] for item in sorted_dict[:2]]
    return lowest_keys


#   sorts a dictionary by descending values
def sort_dict_dec(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict


def sort_dict_asc(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1])
    return sorted_dict


#   flattens a dictionary that contains sub dictionaries
def flatten(dictionary):
    flattened = {key: value for sub_dict in dictionary.values() for key, value in sub_dict.items()}
    return flattened
