"""
Module 2 Assignment by Diandra O'Connor 1/18/23
Updated file with 3 functions related to gymnastics.

Use built-in functions and 
functions from the math module.

Illustrate the ability to call functions and 
display useful results to the user. 

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
        area = length * width 
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here 

def gymnast1_avg_beam_score(*scores):
    """Return average beam score."""
    return sum(scores) / len(scores)


def gymnast_all_around_score(*scores):
    """Return all around score (the sum of all individual event scores)."""
    return math.fsum(scores)


def competition_leo_with_tax(price):
    """Return competition leotard cost with tax.""" # assuming a tax rate of 8%
    return price * 1.08 



# -------------------------------------------------------------
# Call some functions and execute code!


if __name__ == "__main__":

    # calling functions and sharing results with user
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
