
# For statistic operation
from library.math_tool_box import StatMaker

# for random number generator
from library.linear_congruedntial_generator import random_number_gen

# For measuring elapsed time elapsed
from library.measure_time_performance import measure_elapsed_time



###     1. Generate 5 random numbers
random_number_list = random_number_gen( length =5 )

print("\n 5 random numbers are generated as below:")
print( random_number_list )
print()


###     2. Generate N random numbers between -1 and 1, and calculates their average and standard deviation.
# Note: N = 10^1, 10^2, 10^3, 10^4, 10^5

###     3. Measure elapsed time of random number generation on each iteration.

###     4. Design and implemnet a random number generator
# Note: This item is completed, and it is saved in library.linear_congruedntial_generator

size_array = []
output_array = []

for n in range( 1, 6 ):
    size_array.append( 10**n )

for i in range( 0, 5 ):

    length = size_array[i]
    output_array.append( measure_elapsed_time(random_number_gen, length, -1, 1, True ) )

    statistic_info = StatMaker( output_array[i] )

    print("Average of list with length {0} = {1}".format( length, statistic_info.get_avg() ) )
    print("Standard deviation of list with length {0} = {1}".format( length, statistic_info.get_std() ) )
    print()



'''

Example output:

###     1.  Generate 5 random numbers

 5 random numbers are generated as below:
[1255046, 452783350, 1364012331, 390612681, 358303891]



###     2. Generate N random numbers between -1 and 1, and calculates their average and standard deviation.
            N = 10^1, 10^2, 10^3, 10^4, 10^5

###     3. Measure elapsed time of random number generation on each iteration.

###     4. Design and implemnet a random number generator
            This item is completed, and it is saved in library.linear_congruedntial_generator

random_number_gen took 0.031289000 ms to run
Average of list with length 10 = 0.12344294369541378
Standard deviation of list with length 10 = 0.6970713923615578

random_number_gen took 0.168960000 ms to run
Average of list with length 100 = 0.04805143085126898
Standard deviation of list with length 100 = 0.5999758690220189

random_number_gen took 1.527465000 ms to run
Average of list with length 1000 = 0.0023875394355389636
Standard deviation of list with length 1000 = 0.5877759267632492

random_number_gen took 15.660929000 ms to run
Average of list with length 10000 = -0.004161540137474938
Standard deviation of list with length 10000 = 0.5781747512114019

random_number_gen took 153.725024000 ms to run
Average of list with length 100000 = -0.0035780554856993775
Standard deviation of list with length 100000 = 0.5787522721242679

'''