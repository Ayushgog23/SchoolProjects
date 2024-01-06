"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-11-14"
-------------------------------------------------------
"""


def winner():
    """
    -------------------------------------------------------
    description: user provides input about two teams. 
    functions shows the user how many times the string "blue" 
    appeared in the input and how many times the string "grey" 
    appeared in the input.
    Use: blue, grey = winner()
    -------------------------------------------------------
    Parameters:
        winning - enter the winning team (str)
    Returns:
        blue - how many times "blue" was inputted (int)
        grey - how many times "grey" was inputted (int)
    ------------------------------------------------------
    """
    blue = 0
    grey = 0
    winning = input("Enter the winning team (str): ")
    if winning == "blue":
        blue += 1
    elif winning == "grey":
        grey += 1

    while winning != "":
        winning = input("Enter the winning team (str): ")
        if winning == "blue":
            blue += 1
        elif winning == "grey":
            grey += 1

    return blue, grey


def is_prime(num):
    """
    -------------------------------------------------------
    Determines if num is a prime number.
    Use: prime = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int > 1)
    Returns:
        prime - True if num is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    i = 2
    prime = True
    while num > 1:
        num = int(input("Enter a positive integer (int > 1): "))
        if num % 2 == 0:
            prime = False
            print(f"{prime}")
            i = i + 1
        elif num % 2 != 0:
            prime = True
            print(f"{prime}")

    return prime


def interest_table(principal, rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal, rate, payment)
    -------------------------------------------------------
    Parameters:
        principal - original value of a loan (float > 0)
        rate - yearly interest rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print()
    print(f"Principal: {rate}")
    print(f"Interest rate: {rate}%")
    print(f"Monthly payment: {payment}")

    month = 1

    print("-" * 40)
    print(f"Month   Interest    Payment    Balance")
    print("-" * 40)
    while principal > 0:
        interest = principal * rate / 1200
        principal = principal - payment + interest
        if principal < 0:
            payment = payment + principal
            principal = 0
        print(f"{month:>5} {interest:>10.2f} {payment:>11.2f} {principal:>12.2f}")
        month += 1

    return None


def digit_count(num):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: count = digit_count(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int)
    Returns:
        count - the number of digits in num (int)
    ------------------------------------------------------
    """

    count = 0
    if num < 0:
        num = num * -1

    while num > 0:
        num = num // 10
        count += 1
    return count

    if num == 0:
        count = 1
        return count


def sum_factors(num):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_factors(num)
    -------------------------------------------------------
    Parameters:
        num - a positive integer (int >= 1)
    Returns:
        total - the total of num's factors (int)
    ------------------------------------------------------
    """

    total = 0
    i = 1
    while i < num:
        remainder = num % i
        i += 1
        if remainder == 0:
            total += 1

    return total


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
