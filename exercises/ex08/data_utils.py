"""EX08 - Functions made for the data_wrangling file."""
__author__ = "730610651"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Return a list of values from the column header."""
    return_list: list[str] = []
    for row in table:
        return_list.append(row[key])
    return return_list


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one represnted as a dictionary of columns."""
    return_dict: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for key in first_row:
        return_dict[key] = column_values(table,key)
    return return_dict


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each parameter."""
    return_dict: dict[str, list[str]] = {}
    for key in table.keys():
        if rows >= len(table[key]):
            return_dict = table
            return return_dict
        empty_list: list[str] = list()
        row_idx: int = 0
        row_working: list[int] = table[key]
        while row_idx < rows:
            empty_list.append(row_working[row_idx])
            row_idx += 1
        return_dict[key] = empty_list
    return return_dict


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    return_dict: dict[str, list[str]] = {}
    for column in columns:
        empty_list: list[str] = list()
        if column in table:
            row_working: list[str] = table[column]
            for value in row_working:
                empty_list.append(value)
        return_dict[column] = empty_list
    return return_dict


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined"""
    return_table: dict[str, list[str]] = {}
    for column in table1:
        return_table[column] = table1[column]
    for column in table2:
        if column in return_table:
            return_table[column] += table2[column]
        else:
            return_table[column] = table2[column]
    return return_table


def count(list1: list[str]) -> dict[str, int]:
    """Produce a dict where each key is a unique value in the given list and each value associated is the count of the number of times that value appread in the input list."""
    return_dict: dict[str, int] = {}
    for key in list1:
        if key in return_dict:
            return_dict[key] += 1
        else:
            return_dict[key] = 1
    return return_dict