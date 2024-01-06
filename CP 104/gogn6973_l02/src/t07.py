"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-09-22"
-------------------------------------------------------
"""
# Inputs
Number_of_flyers = int(input("Enter the number of flyers: "))
Number_of_Volunteers = int(input("Enter the number of volunteers: "))

# Calculations
Flyers_per_volunteer = Number_of_flyers // Number_of_Volunteers
Flyers_left_over = Number_of_flyers % Number_of_Volunteers

# Output
print("Flyers per volunteer: ", Flyers_per_volunteer)
print("Flyers left over: ", Flyers_left_over)


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
