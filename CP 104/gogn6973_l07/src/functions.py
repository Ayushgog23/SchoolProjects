"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-11-04"
-------------------------------------------------------
"""
from random import randint


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    count = 0
    number = randint(1, high)
    guess = int(input("Enter a guess: (Int>0): "))
    while guess != number:
        if guess > number:
            print("try again - too high")
            guess = int(input("Enter a guess (int>1): "))
            count += 1
            print(f"you guessed {count} times")
        elif guess < number:
            print("try again - too low")
            guess = int(input("Enter a guess (int>1): "))
            count += 1
            print(f"you guessed {count} times")

    print("you got the number!")
    print(f"you guessed {count} times")


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    while target >= 0:
        power = 2 ** target
        print(f"{power}")
        target = int(input("enter a value to find the nearest power of 2: "))

    print("Error")


def num_categories():
    """
    -------------------------------------------------------
    Asks a user to enter a series of numbers, then counts and returns
    how may positives, negatives, and zeroes there are.
    Stop processing values when the user enters -999.
    Use: negatives, zeroes, positives = num_categories()
    -------------------------------------------------------
    Returns:
        negatives - number of negative values (int)
        zeroes - number of zero values (int)
        positives - number of positive values (int)
    ------------------------------------------------------
    """
    number = int(input("first value: "))
    positives = 0
    negatives = 0
    zeroes = 0
    while number != -999:

        if number > 0:
            positives += 1
        elif number < 0:
            negatives += 1
        elif number == 0:
            zeroes += 1
        number = int(input("Next value: "))
    return negatives, zeroes, positives


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    b_total = 0
    l_total = 0
    s_total = 0
    a_total = 0

    away = "Y"

    while away != "N":
        b_total += float(input("How much was breakfast? $"))
        l_total += float(input("How much was lunch? $"))
        s_total += float(input("How much was supper? $"))
        a_total = (b_total + l_total + s_total)
        print(f"Your total for the day was ${a_total}")
        away = str(input("Were you away another day (Y/N)? "))

    return b_total, l_total, s_total, a_total


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    while True:
        value = int(input('Enter the value between ' +
                          str(low) + ' and ' + str(high) + ' : '))
        if value >= low and value <= high:
            return value
        elif value < low:
            print("Value entered is too low")
        else:
            print("Value entered is too high")


def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
        name - description (type)
    ------------------------------------------------------
    """
