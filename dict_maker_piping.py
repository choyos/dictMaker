#!/usr/bin/python
from __future__ import print_function, division

# Get start string in order to know when to start
def get_start_str(lenght):
    start_str = ""
    for i in range(lenght):
        start_str = start_str + "0"
    return start_str

# Get end string in order to know when to end
def get_end_str(lenght):
    end_str = ""
    for i in range(lenght):
        end_str = end_str + "z"
    return end_str

# Rule apply to string
def same_char_togethers(str_var):
    count = 0
    for char in str_var:
        count = count + 1
        if count == 1:
            pre_char = char
        if count != 1:
            if char == pre_char:
                return True
            else:
                pre_char = char
    return False

# Rule apply to string
def three_chars_in_str(str_var):
    for char in str_var:
        if str_var.count(char) > 2:
            return True
    
    return False

# Filters in order to improve result
def filter_str(str_var):
    
    if same_char_togethers(str_var):
        return False
    if three_chars_in_str(str_var):
        return False
    
    return True

# Fcn to increment value
def inc_char(chr_var):
    ascii_chr_var = ord(str(chr_var))
    if ascii_chr_var == 122:
        ascii_chr_var = 48
    elif ascii_chr_var == 57:
        ascii_chr_var = 65
    elif ascii_chr_var == 90:
        ascii_chr_var = 97
    else:
        ascii_chr_var = ascii_chr_var + 1
    return chr(ascii_chr_var)

# Fcn to increment string
def inc_str(str_var, first_level_flag):
    count = 0
    new_str = ""
    next_char = False
    i_aux = 0
    for char in str_var:
        count = count + 1
        if count == 1 or next_char:
            char = inc_char(char)
            next_char = False
            i_aux = count
            if char == '0':
                next_char = True

        new_str = new_str + char
    
    # Check for string validity
    substr_start = new_str[:i_aux]
    substr_end = new_str[i_aux:]
    while not filter_str(substr_end) and first_level_flag:
        substr_end = inc_str(substr_end, False)
    
    new_str = substr_start + substr_end
    return new_str
    
def generate_dict(filename):
    '''
    generate_dict receive as parameter the filename where to store values.
    Generate combinational of lenght receive as parameters
    It uses only ascii parameters:
    - (48-57)/(0-9)
    - (65-90)/(A-Z)
    - (97-122)/(a-z)
    '''
    pass_lenght = 20
    start_str = get_start_str(pass_lenght)
    start_str = "98987676545432321010"
    end_str = get_end_str(pass_lenght)
    end_str =   "qrqrststuvuvwywyxzxz"
    new_str = start_str
    counter = 0
    if filter_str(new_str):
        print(new_str)
        counter = counter + 1
    while new_str != end_str:
        new_str = inc_str(new_str, True)
        if filter_str(new_str):
            print(new_str)
            counter = counter + 1


'''
Main fcn
Works by parsing input parameters and calling needed fcn
'''
if __name__ == "__main__":
    import sys
    import argparse
    parser = argparse.ArgumentParser(description='DictMaker for getting dictionary for brute force attacks')
    parser.add_argument('-o', '--out', default=None, nargs=1,
                        help='File to store dictionary output')

    args = parser.parse_args()
    filename = 'dict.txt'
    if args.out:
        filename = args.out[0]

    generate_dict(filename) 
