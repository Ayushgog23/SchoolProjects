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
F_length = float(input("Enter the length of the foundation: (m) "))
F_width = float(input("Enter the width of the foundation: (m) "))
F_height = float(input("Enter the height of the foundation: (m) "))
Wall_Height = float(input("Enter the wall height: (m) "))
Cost_concrete = int(input("Enter the cost of concrete: ($/m^3) "))
Cost_bricks = int(input("Enter the cost of bricks: ($/m^2) "))

# Calculations
Concrete_For_Foundation = F_length * F_width * F_height
Cost_total_Concrete = Concrete_For_Foundation * Cost_concrete

Bricks1 = F_length * Wall_Height
Times2one = Bricks1 * 2
Bricks2 = F_width * Wall_Height
Times2two = Bricks2 * 2
Bricks_For_Walls = Times2one + Times2two
Cost_total_Bricks = Bricks_For_Walls * Cost_bricks

Total_Cost = Cost_total_Concrete + Cost_total_Bricks

# Outputs
print()
print(f"Concrete needed for foundation: (m^3) {Concrete_For_Foundation:.2f}")
print(f"Cost of concrete: $ {Cost_total_Concrete:.2f}")
print(f"Bricks neede for walls: (m^2) {Bricks_For_Walls:.2f}")
print(f"Cost of bricks: $ {Cost_total_Bricks:,.2f}")
print(f"Total cost is: $ {Total_Cost:,.2f}")


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
