"""Learning list utility functions."""
__author__ = "730610651"


def only_evens(list1: list[int]) -> list[int]:
    """Given list of integers, return the evens."""
    return_list: list[int] = list()
    for idx in list1:
        if idx % 2 == 0:
            return_list.append(idx)
    return return_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Given two lists, create a new list with one after the other."""
    new_list: list[int] = list()
    for idx in list1:
        new_list.append(idx)
    for idx in list2:
        new_list.append(idx)
    return new_list


def sub(list1: list[int], start: int, end: int) -> list[int]:
    """Create a new list that begins with the start index and ends right before the end index."""
    return_list: list[int] = list()

    if start < 0:
        start = 0
    if end > len(list1) - 1:
        end = len(list1)
    if len(list1) == 0 or start >= len(list1) or end <= 0:
        return return_list

    for idx in range(start, end):
        return_list.append(list1[idx])
    return return_list
