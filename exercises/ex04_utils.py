"""Testing Utility Functions."""
__author__ = "730610651"


def all(list1: list[int], a: int) -> bool:
    """Check to see if a is equal to each index of list1."""
    list1_idx: int = 0

    if len(list1) == 0:
        return False

    while list1_idx < len(list1) - 1:
        if list1[list1_idx] != a:
            return False
        list1_idx += 1
    return True


def max(input: list[int]) -> int:
    """If no length is input, output ValueError."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    """Check if value at certain idx is larger than original max."""
    list1_idx: int = 0
    max = input[0]
    while list1_idx <= len(input) - 1:
        if max < input[list1_idx]:
            max = input[list1_idx]
        list1_idx += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Check if length of lists are the same."""
    if len(list1) != len(list2):
        return False
    
    """check if the values match at each index"""
    list_idx: int = 0
    while list_idx < len(list1) - 1:
        if list1[list_idx] == list2[list_idx]:
            list_idx += 1
        else:
            return False
    return True