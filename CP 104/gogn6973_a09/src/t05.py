"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-12-04"
-------------------------------------------------------
"""
fh = open("students.txt", "r", encoding="utf-8")
marklist = []
IDlist = []
for line in fh:
    n = line.strip().split(",")
    for i in n:
        studentmark = i
        studentID = i
        marklist.append(studentmark)
        IDlist.append(studentID)

print(f"{marklist}")
print(f"{IDlist}")


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
