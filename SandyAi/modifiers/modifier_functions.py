import copy
import forecasting as forecast


#   sets the modifiers to the feature that will give you the highest point value
def set_modifiers(islands):
    """
    Assigns modifier values to each feature based of the current board and the determined benefit of each move.

    :param islands: dict[int, dict[str, int]]
        Contains island numbers and their current feature configuration.

    :return: dict[str, list(int)]
        Dictionary of features and the dice values that count towards those features.\

    :example:
    >>> islands = {1: {'Plants': 1, 'Crab': 1, 'Turtle': 1, 'Seal': 0, 'Tectonic': 1, 'Bird': 0}}
    >>> set_modifiers(islands)
    {'Plants': [1], 'Crab': [], 'Turtle': [], 'Seal': [4,2], 'Tectonic': [5,3], 'Bird': [6]}
    """
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
        if len(new_modifiers[feature]) < 2:
            dice_number = default_modifiers[replace_feature][0]
            new_modifiers[replace_feature] = []
            new_modifiers[feature].append(dice_number)
    return new_modifiers


#   takes a sorted dictionary and extracts the two highest values
def extract_two_highest_values(dictionary):
    """
    Takes the first two values of a dictionary sorted in descending order.

    :param dictionary: dict[str, int]
        Contains keys with integer values.

    :return: list(str)
        The keys of the two highest values in the dictionary.

    :example:
    >>> dict = {'Plants': 3, 'Crab': 1, 'Bird': 5}
    >>> extract_two_highest_values(dict)
    ('Bird', 'Plants')
    """
    sorted_dict = sort_dict_dec(dictionary)
    highest_keys = [item[0] for item in sorted_dict[:2]]
    return highest_keys


def extract_two_lowest_values(dictionary):
    """
    Takes the first two values of a dictionary sorted in ascending order.

    :param dictionary: dict[str, int]
        Contains keys with integer values.

    :return: list(str)
        The keys of the two lowest values in the dictionary.

    :example:
    >>> dict = {'Plants': 3, 'Crab': 1, 'Bird': 5}
    >>> extract_two_lowest_values(dict)
    ('Crab', 'Plants')
    """
    sorted_dict = sort_dict_asc(dictionary)
    lowest_keys = [item[0] for item in sorted_dict[:2]]
    return lowest_keys


#   sorts a dictionary by descending values
def sort_dict_dec(dictionary):
    """
    Sorts a dictionary in descending order of its values.

    :param dictionary: dict[str, int]
        Contains str as keys and int as values.

    :return: list(tuple(str, int))
        List of tuples containing key value pairs in descending order of values

    :example:
    >>> dict = {'Plants': 3, 'Crab': 1, 'Bird': 5}
    >>> sort_dict_dec(dict)
    [('Bird', 5), ('Plants', 3), ('Crab', 1)]
    """
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict


def sort_dict_asc(dictionary):
    """
    Sorts a dictionary in ascending order of its values.

    :param dictionary: dict[str, int]
        Contains str as keys and int as values.

    :return: list(tuple(str, int))
        List of tuples containing key value pairs in ascending order of value

    :example:
    >>> dict = {'Plants': 3, 'Crab': 1, 'Bird': 5}
    >>> sort_dict_asc(dict)
    [('Crab', 1), ('Plants', 3), ('Bird', 5)]
    """
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1])
    return sorted_dict

