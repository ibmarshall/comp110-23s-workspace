"""Testing Utility Functions"""
__author__ = "730610651"

def all(list1: list[int], a: int) -> bool:
    """Given a list and an integer, do all of the integers in the list match the given integer"""
    list1_idx: int = 0
    list1true: bool = False

    while list1_idx < len(list1) - 1:
        if list1[list1_idx] != a:
            return False
        list1_idx += 1
    return True

def max(list1: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    list1_idx: int = 0
    
    while list1_idx <= len(list1) - 1:
        if list1[list1_idx] < list1[list1_idx + 1]:
            list1_idx += 1
    return list1[list1_idx]

def is_equal(list1: list[int], list2: list[int]) -> bool:
    list_idx: int = 0

    while list_idx < len(list1) and len(list2):
        if list1[list_idx] == list2[list_idx]:
            list_idx += 1
        else:
            return False
    return True