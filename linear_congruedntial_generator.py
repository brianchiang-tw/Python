import datetime



# Default parameter value
# length = 1
# seed = second of current system time
# modulus = 2^31-1
# a = 48271
# c = 0

# lcg stands for linear congruential generator
def lcg( length=1, seed=datetime.datetime.now().second, modulus = (2**31 - 1), a=48271, c=0):
    for i in range(length):
        next_seed = (a * seed + c) % modulus
        yield next_seed
        seed = next_seed  



# Random number genertor
def random_number_gen( length = 1, lower_bound = 0, upper_bound = 2**31 - 2, is_float = False ):
    
    list_of_random_num = []
    
    adjustment_factor = ( upper_bound - lower_bound + 1 )

    # create an iterator for the output series of lcg
    iterator_of_random_num = lcg(length)

    while True:
        
        random_number = next( iterator_of_random_num, None)

        if None == random_number:
            break
        else:
            
            if True == is_float:
                random_number = float(random_number)

            # Mapping random number into specificed range interval
            random_number = random_number % adjustment_factor + lower_bound

            list_of_random_num.append( random_number )

    return list_of_random_num



output_int = random_number_gen(length = 5, lower_bound = 10, upper_bound = 20)

# example output:
# [10, 17, 10, 16, 12]
print( output_int )



output_flt = random_number_gen(length = 5, lower_bound = 10, upper_bound = 20, is_float = True)

# example output:
# [10.0, 17.0, 10.0, 16.0, 12.0]
print( output_flt )