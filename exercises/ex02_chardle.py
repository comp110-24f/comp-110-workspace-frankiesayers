"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730674158"


def input_word() -> str:
    # this function will prompt the user to put in their chosen word
    word: str = input(
        "Enter a 5-character word: "
    )  # we are using the input function here to prompt the user to input a 5 letter word and store it as the variable 'word'
    if (
        len(word) != 5
    ):  # if the length of the word is not equal to 5 (must be 5 characters)
        print("Error: Word must contain 5 characters.")  # error message
        exit()  # will cause the program to exit, so that the user is not prompted to input their letter
    print(str("'" + word + "'"))  # returns the original word
    return word


def input_letter() -> str:
    # this function will prompt the user to put in their chosen letter
    letter: str = input(
        "Enter a single character: "
    )  # we use the input function to store the use's chosen letter as the variable 'letter'
    if (
        len(letter) != 1
    ):  # "letter" input must be one character; if not, return error statement and exit
        print("Error: Character must be a single character.")
        exit()
    print(str("'" + letter + "'"))
    return letter


def contains_char(word: str, letter: str) -> None:
    # this function takes the inputs 'word' and 'letter' (as previously defined) and
    # determines the number and location of the instances that the chosen 'letter' occurs in 'word'
    # if put input_word() and input_letter() into parameters, the user is prompted to insert word and char (those functions are called)
    print("Searching for " + letter + " in " + word)
    count: int = 0  # counting the number of instances 'letter' appears in 'word'
    index: int = (
        0  # used to index & check whether the indexed letter of 'word' matches 'letter'
    )
    while index < len(
        word
    ):  # while the index is less than the length of the word (index starts at 0), this while loop will run
        if letter == word[index]:
            # if the chosen letter is the same as the word at a certain index, we add 1 to count and print where we found it
            count += 1
            print(letter + " found at index " + str(index))
        index += 1  # check the next letter

    # Correctly print the number of occurrences
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


def main() -> None:
    # main function
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
