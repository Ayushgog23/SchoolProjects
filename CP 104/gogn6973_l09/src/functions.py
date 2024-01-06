"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:  169026973
Email:  Gogn6973@mylaurier.ca
__updated__ = "2022-11-18"
-------------------------------------------------------
"""


def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    if len(chemical) < 2:
        hydroxide = False
    if chemical[len(chemical) - 2] == "O" and chemical[len(chemical) - 1] == "H":
        hydroxide = True
    else:
        hydroxide = False

    return hydroxide


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """

    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:10]

    return pc, pi, pq


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if three upper-case characters, False otherwise
        digits - True if four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
    -------------------------------------------------------
    """

    # category
    first3 = product_code[0:3]
    CATEGORY = first3.upper()
    ALPHABET = first3.isalpha()

    # digits
    next4 = product_code[3:7]
    Numbersonly = next4.isdigit()

    # qualifiers
    q = product_code[7]
    QUALIFIER = q.upper()
    qualifierletter = q.isalpha()

    if first3 == CATEGORY and ALPHABET == True:
        category = True
    else:
        category = False

    if Numbersonly == True:
        digits = True
    else:
        digits = False

    if q == QUALIFIER and qualifierletter == True:
        qualifiers = True
    else:
        qualifiers = False

    return category, digits, qualifiers


def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    n = len(s)
    i = 0
    count = 0
    while i < n:
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
            count += 1
        elif s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
            count += 1
        i += 1

    return count


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    i = 0
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    n = len(txt)

    while i < n:
        value = txt[i]
        ALPHABET = value.isalpha()
        i += 1
        if value == value.upper() and ALPHABET == True:
            uppr += 1
        if value == value.lower() and ALPHABET == True:
            lowr += 1
        if value.isdigit() == True:
            dgts += 1
        if value.isspace() == True:
            whtspc += 1

    return uppr, lowr, dgts, whtspc


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
