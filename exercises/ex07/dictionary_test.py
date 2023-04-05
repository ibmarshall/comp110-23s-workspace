"""Testing our Dictionary Functions."""
__author__ = "730610651"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_letters() -> None:
    """Use letters as the keys and values of the dictionary."""
    dict1: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(dict1) == {"b": "a", "d": "c", "f": "e"}


def test_invert_words() -> None:
    """Use words as the keys and values of the dictionary."""
    dict1: dict[str, str] = {"dog": "cat", "fish": "snale"}
    assert invert(dict1) == {"cat": "dog", "snale": "fish"}


def test_invert_empty() -> None:
    """Use an empty input dictionary."""
    dict1: dict[str, str] = dict()
    assert invert(dict1) == {}


def test_fav_two_colors() -> None:
    """Input dictionary with just two colors."""
    dict1: dict[str, str] = {"Ro": "Blue", "Jo": "Green", "Zo": "Green"}
    assert favorite_color(dict1) == "Green"


def test_fav_one_color() -> None:
    """Input dictionary with just one color."""
    dict1: dict[str, str] = {"Ro": "Blue", "Jo": "Blue"}
    assert favorite_color(dict1) == "Blue"


def test_fav_same_value() -> None:
    """Have multiple colors with the same values."""
    dict1: dict[str, str] = {"Ro": "Pink", "Jo": "Black", "Bo": "Pink", "Zo": "Black"}
    assert favorite_color(dict1) == "Pink"


def test_count_one_value() -> None:
    """Have one value in the input list."""
    list1: list[str] = ("a", "a", "a")
    assert count(list1) == {"a": 3}


def test_count_two_values() -> None:
    """Have two values in the input list."""
    list1: list[str] = ("a", "a", "b")
    assert count(list1) == {"a": 2, "b": 1}


def test_count_empty() -> None:
    """Input list is empty."""
    list1: list[str] = list()
    assert count(list1) == {}