"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-10-07"
-------------------------------------------------------
"""
# inputs
N_Cake = int(input("Enter the number of pieces of cake: "))
N_Goers = int(input("Enter the number of party goers: "))
# Calculations
Pieces_Per_Goer = int(N_Cake // N_Goers)
Remainder = N_Cake % N_Goers
# Output
print(f"Pieces of cake per party goer: {Pieces_Per_Goer}")
print(f"Cake left over: {Remainder}")


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
