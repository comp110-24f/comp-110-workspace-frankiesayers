"""Conditionals Practice!"""

# write a function called check_first_letter that tapes an input two strs: word and letter"
# it should return "match!" if the first character of word is letter
# otherwise, it should return "no match!"


def check_first_letter(word: str, letter: str) -> None:
    if word[0] == letter:
        print("match!")
    else:
        print("no match!")


check_first_letter(word="kind", letter="k")
