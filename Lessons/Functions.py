"""Practice with Functions"""

"""8/26"""

from random import randint

# print(randint(3, 17))


# function definition
def sum(num1: int, num2: int) -> int:  # parameters
    """a function called “sum” that takes two ints: num1 and num2 as inputs and returns the sum of the two numbers"""
    return num1 + num2


# function call
print(sum(num1=2, num2=13))  # arguments
