with open("3_gear_ratios.txt") as fyle:
    lines = fyle.readlines()

# Sample: (114 and 58 are the only non-numbers)
# sample = "467..114..\n\
# ...*......\n\
# ..35..633.\n\
# ......#...\n\
# 617*......\n\
# .....+.58.\n\
# ..592.....\n\
# ......755.\n\
# ...$.*....\n\
# .664.598.."

# lines = sample.split("\n")
# SUM = 4361


## To get list of symbols ## CAN POSSIBLY USE REGEX
# ls_symbols = []
# for line in lines:
#     for char in line:
#         if char not in ls_symbols and char not in "1234567890.\n":
#             ls_symbols.append(char)

ls_symbols = ['*', '-', '%', '$', '=', '@', '#', '/', '&', '+']

##############
## OPTION 1 ##
##############
# For every SYMBOL found search around it for integers
# If integer found, extend in certain direction to include all digits
# Make sure not to double count numbers



##############
## OPTION 2 ##
##############
# For every INTEGER found, extend to the right until number is finished
# Once number is found, search around it for symbols.
# If there are symbols immediately around the number, add it to the sum


# Option 2:
"""ISSUES:
1. Need to use try and except statements for out of bound lines, but if I put except continue, then the rest of the code (the elifs) will not execute when I want it to
2. Some variables (j, i, and line (unless specified)) are not defined in my is_valid function according to Pylance, not sure how to make it so that the function will call the global variables
    Janky solution: Specify all variables in the is_valid function. ##DONE##
3. Need to find a way to skip the loop a set number of times (if number is 3 digits long, we want to skip checking for the next 2 characters in the line)
    Janky solution: implementation of skip value ##DONE##

"""



def main_2():
    sum = 0
    for i, line in enumerate(lines):
        print(i, f"line = {line}")
        skip = 0
        for j, char in enumerate(line):
            # print(f"Skip = {skip}")
            if skip != 0:
                skip -= 1
                print("skip")
                continue
            if char in "1234567890":
                number = get_number(line, j)
                print(number)
                if is_valid(number, line, i ,j):
                    sum += number
                    print(f"sum ({sum - number}) += {number}")
                skip = len(str(number))

                # Skip the loop [length] number of times
    print(f"SUM = {sum}")

def get_number(line:list, pos:int):
    num_str = "" # keep it as a string to be able to concatenate it, then convert to number
    while line[pos] in "1234567890":
        num_str += line[pos]
        pos += 1

    return int(num_str)

def is_valid(number, line, i, j):
    """Want to make use of the global values of i, and lines"""
    length = len(str(number))

    if line[j-1] in ls_symbols or line[j+length] in ls_symbols:
        return True
    
    else:
        try:
            surroundings = [lines[i-1][j-1:j+length+1], lines[i+1][j-1:j+length+1]] # Check if there should be a + 1
            print(i, lines[i])
            for area in surroundings:
                for symbol in ls_symbols:
                    if symbol in area:
                        return True
        except IndexError:
            pass
        







if __name__ == "__main__":
    main_2()