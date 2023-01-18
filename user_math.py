"""
Module 2 Assignment by Diandra O'Connor 1/18/23
Updated file with 3 functions related to gymnastics.

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)

# average beam score
# a function for average scores on beam
def gymnast1_avg_beam_score(*scores):
    return sum(scores) / len(scores)

# all around score
# using fsum from the math module to show gymnast all-around score
def gymnast_all_around_score(*scores):
    return math.fsum(scores)

# competition leotard cost
# a function for determining cost of competition leotard with tax
def competition_leo_with_tax(price):
    return price * 1.08  # assuming a tax rate of 8%







# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print()

print("The area of lot (6,2) is:", get_area_of_lot(6,2))
print()
print("The area of lot (12,12) is:", get_area_of_lot(12,12))
print()
print(f"The area of lot (10,12) is {get_area_of_lot(10,12)}")
print()

# call function for average beam score
print("Gymnast1 has beam scores of 9.4, 9.55, 9.725, 8.85 and 9.6")
gymnast1_beam_scores = [9.4, 9.55, 9.725, 8.85, 9.6]
print(f"Gymnast1 average beam score is {gymnast1_avg_beam_score(9.4, 9.55, 9.725, 8.85, 9.6)}")
print()

# call function for all around score
print("Gymnast2 has the following scores: vault 9.55, bars 8.8, beam 9.4, floor 9.675")
print(f"Gymnast2 earned an all around score of {gymnast_all_around_score(9.55, 8.8, 9.4, 9.675):.3f}")
print()

# call function for competition leotard cost
print("The gymnasts competition leotard price is $99.99 before taxes")
print()
print(f"The cost of the gymnasts competition leotard with tax is ${competition_leo_with_tax(99.99):.2f}")
print()
