"""Exercise 01: Plan a Cozy Tea Party that determines the # of Tea Bags, Treats, and total cost of a Tea Party based on # of guests"""

__author__: str = "730674158"

# the big picture of the program should be located at the top
# this is why we add main_planner() function to the beginning


def main_planner(guests: int) -> None:
    """Determine the number of tea bags, treats, and final cost of the tea party based on the number of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # Will produce "A Cozy Tea Party for _____ People!"
    print("Tea Bags: " + str(tea_bags(people=guests)))
    # Will produce total number of tea bags
    print("Treats: " + str(treats(people=guests)))
    # Will produce total number of treats
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # Will produce total cost of the party
    # "main" funcitons do not return a value but orchestrate the execution of a program and produce output
    # We must convert the values to strings, or they won't print


def tea_bags(people: int) -> int:
    """Calculate the number of tea bags required for the party if each guests needs 2 tea bags"""
    return people * 2
    # if each guest (denoted as "people") requires 2 tea bags, we can calculate # teabags by multiplying people * 2
    # will return an int that represents the number of tea bags required


def treats(people: int) -> int:
    """Calculate the number of treats required for the party if each guest eats 1.5 treats per tea bag"""
    return int(
        tea_bags(people=people) * 1.5
    )  # must use keyword argument people=people(assign)
    # for each tea bag that a guest drinks, they will eat 1.5 treats, on average
    # since the input of the function treats() is the number of people, we call the tea_bags function to convert the number of guests to tea bags
    # now that we have the number of tea bags at the party, we multiply this figure by 1.5 to find the number of treats
    # the return type is int; therefore, we have to convert our float value that we have from multiplying an int by a float
    # the returned value is the number of treats based on the number of guests attending


def cost(tea_count: int, treat_count: int) -> float:
    """Compute the cost of the tea bags and treats combined based on the number of guests attending the party"""
    return tea_count * 0.5 + treat_count * 0.75
    # each tea bag costs $0.50 and each treat costs $0.75
    # therefore, we multiply the number of teabags by .5 and the number of treats by .75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    # Will ask user about the number of guests attending the party
    # Must come AFTER all code (reference to main_planner, python runs top to bottom)
