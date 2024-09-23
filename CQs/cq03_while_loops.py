"""CQ03: While Loops"""

__author__ = "730674158"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0  # to keep track of how many times search_char appears
    index: int = 0  # to keep track of the position in the string
    while index < len(phrase):
        # check if the current character matches search_char
        if phrase[index] == search_char:
            count += 1
            # if the index(number of char) of the phrase matches the search char itself, it'll add to the count
        index += 1
    return count  # the number of times you find the character!
