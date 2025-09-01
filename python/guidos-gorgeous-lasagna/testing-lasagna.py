#Defining the EXPECTED_BAKE_TIME
'''The expected bake time is a constant value that represent how much time the lasagna will take.
'''
EXPECTED_BAKE_TIME = 40
print(EXPECTED_BAKE_TIME)

def bake_time_remaining(baketime=0):

    '''Calculating the remaining bake time
    param: number_of_mins
    param: EXPECTED_BAKE_TIME
    returns the remaining minutes the lasagna needs to be in the oven
    '''
   
    bake_time_remaining = EXPECTED_BAKE_TIME - baketime 
    return bake_time_remaining

total = bake_time_remaining()
print(total)

