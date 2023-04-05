"""Practice with Dictionaries."""
__author__ = "730610651"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, invert the keys and the values."""
    return_dict: dict[str, str] = dict()
    # invert the keys and values
    for key in dict1:
        """If there are multiple of the same values in the input dictionary, return KeyError."""
        if dict1[key] in return_dict:
            raise KeyError("KeyError")
        return_dict[dict1[key]] = key
    return return_dict


def favorite_color(dict1: dict[str, str]) -> str:
    """Return the color that appears the most frequently."""
    dict2: dict[str, int] = dict()
    # create a new dictionary with the colors and amount of times they are listed
    for name in dict1:
        if dict1[name] in dict2:
            dict2[dict1[name]] += 1
        elif dict1[name] not in dict2:
            dict2[dict1[name]] = 1
    
    color_idx: int = 0
    fav_color: str = ""
    # find the color with the most mentions
    for color in dict2:
        if dict2[color] > color_idx:
            fav_color = color
            color_idx = dict2[color]
    return fav_color


def count(list1: list[str]) -> dict[str, int]:
    """Count the frequency a value is mentioned in the list."""
    return_dict: dict[str, int] = dict()
    # add the values to the dictionary
    for value in list1:
        if value in return_dict:
            return_dict[value] += 1
        elif value not in return_dict:
            return_dict[value] = 1
    return return_dict