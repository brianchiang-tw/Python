import functools
import random
import math

class StatMaker:
    container = []
    size = 0

    def __init__(self, new_list):
        self.container = new_list
        self.size = len(self.container)

    # Get the minimum value of a series
    def get_min(self):
        min_value = functools.reduce( lambda smallest, x: smallest if smallest < x else x, self.container, self.container[0] )
        return min_value

    # Get the maximum value of a series
    def get_max(self):
        max_value = functools.reduce( lambda largest, x: largest if largest > x else x, self.container, self.container[0] )
        return max_value

    # Get the summation of a series
    def get_sum(self):
        sum_value = functools.reduce( lambda sum, x: sum + x, self.container, 0 )
        return sum_value

    # Get the average of a series
    def get_avg(self):
        avg = self.get_sum() / self.size
        return avg

    # Get the standard deviation of a series
    def get_std(self):
        # Recall:
        # var = { (  sigma[ (Xi - avg )^2 ]   ) / (N-1) } 
        #     = { ( sigma[ Xi^2 ] - N * avg^2 ) / (N-1) } 

        # std = sqrt(var)

        sum_of_element_square = functools.reduce( lambda sum, x: sum + x**2, self.container, 0 ) 
        N_of_avg_square = self.size * self.get_avg()**2

        var = ( sum_of_element_square - N_of_avg_square) / ( self.size-1 )
        std = var**( 1/2 )

        return std



### Tutorial:

# list_test = list( range(1,6) )

# [1, 2, 3, 4, 5]
# print( list_test )

# random.shuffle( list_test )

# example output:
# [3, 1, 2, 5, 4]
# print( list_test )

# stat_info = StatMaker(list_test)
# min_value = stat_info.get_min()
# max_value = stat_info.get_max()
# sum_value = stat_info.get_sum()
# avg_value = stat_info.get_avg()
# std_value = stat_info.get_std()




# 1
# print( min_value )

# 5
# print( max_value )

# 15
# print( sum_value )

# 3.0
# print( avg_value )

# 1.5811388300841898
# print( std_value )




