"""Practice with Conditionals"""

# writing a function


def less_than_10(num: int) -> None:
    """Tell me if num is <10."""
    if num < 10:
        print("Small Number!")
    else:
        print("Big Number!")
    print("Have a nice day!")


less_than_10(num=11)
