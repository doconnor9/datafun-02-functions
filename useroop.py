""" Module 2, Task 5
Diandra O'Connor 1/21/23

Updating PyBuddy to be relevant to my domain: gymnastics

added/modified attributes, created new methods related to my domain

""" 


import datetime
from enum import Enum
import statistics
import random


class Species(Enum):
    DOG = 1
    CAT = 2
    ELF = 3
    HUMAN = 4


class PyBuddy:
    """ PyBuddy class for creating a buddy."""

    def __init__(self, name, species, num_legs, weight_kgs, is_available, skill_list, 
    floor_score_list, leo_color):
        """ Built-in method to create a new instance."""
        self.name = name
        self.species = species
        self.num_legs = num_legs
        self.weight_kgs = weight_kgs
        self.is_available = is_available
        self.skill_list = skill_list
        self.create_date = datetime.datetime.now()
        self.floor_score_list = floor_score_list
        self.leo_color = leo_color

    def __str__(self):
        """Built-in method to return a string describing this instance."""
        s0 = f"I'm {self.name}.\n"
        s1 = f"I'm a {self.species} with {self.num_legs} legs.\n"
        s2 = f"I weigh {self.weight_kgs:.2f} kgs.\n"
        s3 = f"I've been alive for {self.get_age_string()}.\n"
        

        if self.is_available:
            s4 = "I'm available for performing.\n"
        else:
            s4 = "Sorry, I'm too tired for performing today.\n"

        s5 = "I know how to do:\n"

        s6 = ""
        for skill in self.skill_list:
            s6 = s6 + f"  - {skill}\n"

        s = s0 + s1 + s2 + s3 + s4 + s5 + s6
        return s

    def get_age_string(self):
        """Return the age as a string."""
        start = self.create_date
        end = datetime.datetime.now()
        duration = end - start
        ageString = str(duration)
        return ageString

    def display_welcome(self):
        print()
        print("Welcome, I'm a new PyBuddy.\n")
        # print using our built-in to string method
        print(self.__str__())


 # new methods added 
    def high_floor_score(self):
        """Return highest floor score from attribute list."""
        return max(self.floor_score_list) 
    
    def mean_floor_score(self): 
        """Return average floor score from attribute list.""" 
        return statistics.mean(self.floor_score_list)    
        
    def slim_weight(self):  
        """Return weight reduced by 10%."""
        return (self.weight_kgs - (self.weight_kgs * 0.1))
    
    def bulk_up_weight(self):
        """Return weight increased by 10%."""  # muscle of course :) 
        return (self.weight_kgs + (self.weight_kgs * 0.1))

    def get_favorite_leo_color(self):
        """Return favorite leo color.""" # using random selection from attribute list
        return random.choice(self.leo_color)    


# -------------------------------------------------------------
# Call some functions and execute code!

# if this is the main file being run

if __name__ == "__main__":
    # Create an instance of a PyBuddy

    nadia = PyBuddy(
        "Nadia",
        Species.HUMAN,
        2,
        54.5,
        True,
        ["backhandsprings", "turns", "a double full", "a release move", "a perfect 10.0 routine"],
        [9.8, 9.9, 9.6, 9.75, 10.0],
        ["blue", "red", "purple", "black", "anything sparkly"]
    )

    # Call the buddy's welcome() method
    nadia.display_welcome()


    # display information about weight, scores and leotard color to user
    print()
    print(f"If I lose 10% of my body weight, I will weigh {nadia.slim_weight():.1f} kgs")
    print()
    print(f"My average floor score this season is {nadia.mean_floor_score():.2f}")
    print()
    print(f"My highest floor score so far is {nadia.high_floor_score()}")
    print()
    print(f"The color of my favorite leotard is {nadia.get_favorite_leo_color()} ")
    print()

 # -----------------------------------------------------


    # Create another instance of a PyBuddy
    bart = PyBuddy(
        "Bart",
        Species.HUMAN,
        2,
        72.7,
        True,
        ["flares", "a triple twist", "a tkatchev", "a tsukahara", "an iron cross"],
        [14.4, 13.8, 14.6, 13.55, 14.8],
        ["black", "blue", "green", "red"]
    )


    # Call the buddy's welcome() method
    bart.display_welcome()


     # display information about weight, scores and leotard color to user
    print()
    print(f"If I gain 10% of my body weight, I will weigh {bart.bulk_up_weight():.1f} kgs")
    print()
    print(f"My average floor score this season is {bart.mean_floor_score():.2f}")
    print()
    print(f"My highest floor score so far is {bart.high_floor_score()}")
    print()
    print(f"The color of my favorite leotard is {bart.get_favorite_leo_color()} ")
    print()