"""Practice with Conditionals"""

# def less_than_10(num: int) -> None:
#   """Tell me if num is <10"""
#  dub: int = num * 2
# dub = dub - 1
# print(dub)
# if num < 10:
#  print("small number")
# else:
#   print("big number")
# print("have a nice day!")


# less_than_10(num=5)


def get_weather_report() -> str:
    """Display weather instructions."""
    weather: str = input("What is the weather?")
    # defining weather using new input variable
    if weather == "rainy" or weather == "cold":
        # need == sign;
        # cannot just have OR operator because OR takes what is on either side as Booleans and tries to evaluate
        # have boolean on either side of that operator!
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
