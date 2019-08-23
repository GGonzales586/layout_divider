#! Python3
# layout_divider.py - A program to calcuate layout along a defined length of space.
# This program will produce the result that will have an equal distance between all fixtures and the walls.

import time

def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac

def equal_empty_space():
    while True:
        fixture_count = float(input('How many fixtures are to be fitted in the space?\n'))
        fixture_length = convert_to_float(input('How long are the fixtures? (Fractional inches)\n'))
        total_fixture_length = fixture_count * fixture_length
        space_length = convert_to_float(input('How long is the space? (Fractional inches)\n'))
        empty_space = (space_length - total_fixture_length) / (fixture_count + 1)
        print('The empty space between fixture to fixture and the walls is...\n' + str(empty_space))
        input('Hit enter to continue.\n')
        break

# Add function to produce a half length at the ends.

def half_empty_space():
    while True:
        fixture_count = float(input('How many fixtures are to be fitted in the space?\n'))
        fixture_length = convert_to_float(input('How long are the fixtures? (Fractional inches)\n'))
        total_fixture_length = fixture_count * fixture_length
        space_length = convert_to_float(input('How long is the space? (Fractional inches)\n'))
        fix_wall_layout_oc = fixture_length / 2
        fix_fix_layout_oc = (space_length - total_fixture_length - fixture_length) / (fixture_count - 1)
        print('The distance between fixture to fixture and the walls O.C. is...\n' + str(fix_fix_layout_oc))
        print('The distance between fixture to wall is...\n' + str(fix_wall_layout_oc))
        input('Hit enter to continue.\n')
        break

while True:
    layout_choice = input("""What layout method do you need today?\nThe choices are...\n
1 - Layout with equal empty space between fixtures and the end walls.\n
2 - Layout with equal empty space between fixtures and half space between
the outside fixtures and the end walls.\n
3 - Close program.\nEnter a number to decide\n""")


    if layout_choice == '1':
        equal_empty_space()
    elif layout_choice == '2':
        half_empty_space()
    elif layout_choice == '3':
        print('Pleasure serving you master.\n')
        break
    else:
        print('Try that again brainiac.\n')
        continue
