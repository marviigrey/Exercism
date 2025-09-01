"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
#PREPARATION_TIME = 0
print("The expected bake time: " + str(EXPECTED_BAKE_TIME) + "mins")


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining():
    '''A function that defines or calculate the bake time remaining to the expected bake time.'''
    
    baketime = input("\n\nactual minutes the lasagna has been in the oven?\n")
    new_baketime = int(baketime)
   
    new_baketime = EXPECTED_BAKE_TIME - new_baketime
    print(f"\nbake time remaining is: {new_baketime}\n")
    # new_baketime=EXPECTED_BAKE_TIME - baketime
    # print("you have" + new_baketime + "mins remaining")
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
print(f"Please Note: The preparation time per layer is:{PREPARATION_TIME} mins")
def preparation_time_in_minutes(number_of_layers):
    '''This function helps to calculate the time taken to prepare the lasagna.'''
    layers = input("\n how many layers of lasagna are you preparing\n")
    number_of_layers = int(layers)
    
    return number_of_layers * PREPARATION_TIME

total = preparation_time_in_minutes(number_of_layers=0)
print(f"Great! It will take {total} minutes to prepare the lasagna.")




# #TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
   layers = input("\n how many layers of lasagna are you preparing\n")
   layers = int(layers)
   number_of_layers = layers * 2
   print(f"it will take {number_of_layers} mins to prepare the lasagna.\n")

   elapsed_bake_time = input("how long have we spent making the lasagna?\n")
   elapsed_bake_time = int(elapsed_bake_time)

   return elapsed_bake_time + number_of_layers

 #     '''This functions calculate the elapsed time taken after expected bake time is passed.'''

   
total_mins = elapsed_time_in_minutes(number_of_layers=0, elapsed_bake_time=0)
print(f"\nThe elapsed time spent in the making the lasagna is {total_mins} mins")

# # TODO: Remember to go back and add docstrings to all your functions
# #  (you can copy and then alter the one from bake_time_remaining.)