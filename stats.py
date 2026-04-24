from typing import TypedDict


# return number of words in str
def get_word_count(content: str):
    return len(content.split())


# return dict of all char counts
def get_char_counts(content: str):
    counts: dict[str, int] = {}

    for char in content:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


class CharCount(TypedDict):
    char: str
    num: int


def sort_by_num(dict: CharCount):
    return dict["num"]


# return array of sorted dicts of chars and counts
def sort_char_counts(counts_dict: dict[str, int]):
    counts_array: list[CharCount] = []

    for key in counts_dict:
        counts_array.append({"char": key, "num": counts_dict[key]})

    counts_array.sort(reverse=True, key=sort_by_num)
    return counts_array
