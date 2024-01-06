"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ayush Gogne
ID:      169026973
Email:   gogn6973@mylaurier.ca
__updated__ = "2023-01-20"
-------------------------------------------------------
"""
from pickle import TRUE, FALSE
def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    
    # Values: [1, 2, 0, 1, 4, 1, 1, 2, 2, 5, 4, 3, 1, 3, 3, 4, 2, 4, 3, 1, 3, 0, 3, 0, 0]
    # Cleaned: [1, 2, 0, 4, 5, 3]
    
    i = 0
    values_list = []
    while i < len(values):
        if values[i] in values_list:
            values.pop(i)
        else:
            values_list.append(values[i])
            
    values = values_list
        
                    
    print(values)
                    
    return None
            
    
def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0
    
    line = fv.readline()
    while line != "":
        stringedline = str(line)
        for i in stringedline:
            if i.isupper():
                u += 1
            elif i.islower():
                l += 1
            elif i.isdigit():
                d += 1
            elif i.isspace():
                w += 1
            else:
                r += 1
        line = fv.readline()
        
    return u, l, d, w, r
                
                
def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """
    locations = []
    for i in range(0,len(string),1):
        for j in range(i,len(string),1):
            if string[i:j] == sub:
                locations.append(i)
        
    return locations
            
            
def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    noremainder = 0
    if year % 4 == noremainder and year > 0:
        leap_year = True
    elif year > 0:
        leap_year = False
    else:
        leap_year = "Not a year greater than 0"
    
    return leap_year
            
        
def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """             
    
    firstvalue = name[0]
    if firstvalue.isalpha() or firstvalue == "_":
        for i in range(0,len(name),1): 
            if name[i].isupper() or name[i].islower() or name[i].isdigit() or name[i] == "_":
                valid = True
            else: 
                valid = False
    else:
        valid = False
        
    return valid
            
    
def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    #a = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
    #   j   0  1    0  1    0  1    0  1    0  1
    #   i     0       1       2      3       4
    
    matrix = []
    for i in range(0,len(a),1):
        for j in range(0,len(a[i])):
            row = []
            row.append(a[i][j])
            matrix.append(row)
    
    result = []
    for k in range(0,len(a[i]),1):
        rowresult = [] 
        for j in range(0,len(a),1):
            rowresult.append(0)
        result.append(rowresult)

            
    return matrix, result


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    # a = [[2,2],     b = [[1,1,1,1]
    #      [2,2],          [1,1,1,1]]
    #      [2,2]]
    
    result = []
    for i in range(len(a)):
        for j in range(len(b)):
            row = []
            for z in range(len(b[j])):
                row.append(0)
        result.append(row)
                

    for c in range(len(a)):
        for d in range(len(a[c])):
            for e in range(len(b)):
                result[c][d] += a[c][e]*b[e][d]
                
    return result
            
def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    # car
    # 012
    
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        pl = word + "way"
        
    elif word[0] != "a" and word[0] != "e" and word[0] != "i" and word[0] != "o" and word[0] != "u":
        if word[0].isupper():
            ending = word[0].lower() + "ay"
            fullword = word + ending
            replacedfullword = fullword.replace(word[0],"",1)
            capitalfirst = replacedfullword[0].upper()
            pl = capitalfirst + replacedfullword[1:]

        elif word[0].islower():
            ending = word[0] + "ay"
            fullword = word + ending
            replacedfullword = fullword.replace(word[0],"",1)
            pl = replacedfullword
            
    return pl
        

def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    estring = ""
    lstring = string.lower()
    for i in range(0,len(lstring),1):
        for j in range(0,len(alphabet),1):
            if lstring[i] == alphabet[j]:
                estring += alphabet[j+n].upper()
                    
    return estring