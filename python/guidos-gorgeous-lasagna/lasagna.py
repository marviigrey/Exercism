"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
#PREPARATION_TIME = 0


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(baketime):
    '''A function that defines or calculate the bake time remaining to the expected bake time.'''
    time = input(f"how many minutes does it take to bake?")
    time = baketime

    baketime=EXPECTED_BAKE_TIME - baketime
    print(baketime)
    
   # elapsed_bake_time = new_bakeTime - EXPECTED_BAKE_TIME
    #print(f"it will take {elapsed_bake_time.__abs__()} mins more to complete")
    #return elapsed_bake_time
    

    
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
bake_time_remaining()
'''This function helps to calculate the '''

#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
#def preparation_time_in_minutes():
PREPARATION_TIME = 2
def preparation_time_in_minutes(number_of_layers):
    '''This function helps to calculate the time taken to prepare the lasagna.'''
    
    number_of_layers = PREPARATION_TIME * number_of_layers
    print(number_of_layers)
        
         


preparation_time_in_minutes()





#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''This functions calculate the elapsed time taken after expected bake time is passed.'''

    number_of_layers = PREPARATION_TIME * number_of_layers
    bake_time = EXPECTED_BAKE_TIME - bake_time
    elapsed_bake_time = bake_time + number_of_layers
    print(elapsed_bake_time)

elapsed_time_in_minutes()

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)