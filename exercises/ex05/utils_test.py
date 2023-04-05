"""EX05 Utility Test."""
__author__ = "730610651"

from exercises.ex05.utils import only_evens, concat, sub

# only_evens


def test_normal_list() -> None:
    """Test a simple, chronological set."""
    test_list: list[int] = [1, 2, 3, 4]
    assert only_evens(test_list) == [2, 4]


def test_empty_list() -> None:
    """Use an empty list."""
    test_list: list[int] = list()
    assert only_evens(test_list) == []


def test_zero() -> None:
    """Use zero in sequence."""
    test_list: list[int] = [-2, 0, -4, 4]
    assert only_evens(test_list) == [-2, 0, -4, 4]
 

# concat


def test_normal_lists() -> None:
    """Test two lists of positive integers in a row."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [4, 5, 6]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6]


def test_list_lengths() -> None:
    """Use two lists of different lengths."""
    test_list1: list[int] = [1, 2, 3, 4]
    test_list2: list[int] = [5, 6, 7]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6, 7]


def test_one_empty() -> None:
    """Use one complete and one empty list."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = list()
    assert concat(test_list1, test_list2) == [1, 2, 3]


# sub


def test_end_idx() -> None:
    """Test if end idx is greater than the length of the sequence."""
    test_list: list[int] = [2, 3]
    assert sub(test_list, 0, 1) == [2]


def test_start_idx_negative() -> None:
    """Test if the start idx is negative."""
    assert sub([1, 2, 3], -1, 2) == [1, 2]


def test_start_idx_zero() -> None:
    """Start with idx of zero."""
    assert sub([1, 2, 3], 0, 2) == [1, 2]