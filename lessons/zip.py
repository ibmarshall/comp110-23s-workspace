"""CQ04 - Zip Functions."""
___author___ = "730610651"

def zip(list1: list[str], list2: list[int]) -> dict[str,int]:
    new_dict: dict[str, int] = {}

    if len(list1) != len(list2):
        return new_dict
    
    if len(list1) or len(list2) == 0:
        return new_dict
    
    for key in range(len(list1)):
        new_dict[list1[key]] = list2[key]
    return new_dict