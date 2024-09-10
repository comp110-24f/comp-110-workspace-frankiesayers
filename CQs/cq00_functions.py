"""My first Challenge Question!"""

"""CQ00"""

__author__ = 730674158


def mimic(message: str) -> str:
    "A function that returns a given message back to the user"
    return message


def main() -> None:
    "A funciton that will print the result of calling mimic"
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
