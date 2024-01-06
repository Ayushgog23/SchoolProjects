"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-10-22"
-------------------------------------------------------
"""
# Imports
from functions import gym_cost
# Constants
cost = float(input("membership cost: $"))
friends = int(input("Number of friends signed up: "))
final_cost = gym_cost(cost, friends)
print(f"Your membership cost is ${final_cost:.2f}")


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
