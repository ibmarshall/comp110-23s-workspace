def odd_and_even(list1: list[int]) -> list[int]:
    list2: list[int] = list()
    list_idx: int = 0
    for idx in list1:
        if idx % 2 == 1 and list_idx %2 == 0:
            list2.append(idx)
        list_idx += 1
    return list2

def value_exists(dict1: dict[str, int], int1: int) -> bool:
    for idx in dict1:
        if dict1[idx] == int1:
            return True
    return False

def short_words(list1: list[str]) -> list[str]:
    """Return list of words that are shorter than 5 characters."""
    list2: list[str] = list()
    for words in list1:
        if len(words) < 5:
            list2.append(words)
        elif len(words) >= 5:
            print(f"{words} is too long!")
    return list2