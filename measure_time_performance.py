import time

def measure_target():
    time.sleep(5)
    return


time1 = time.perf_counter()

measure_target()

time2 = time.perf_counter()

# example output:
# measure_target took 4.993910050 second to run
# measure_target took 4993.910050000 ms to run
# measure_target took 4993910.050000000 μs to run
print('{:s} took {:.9f} second to run'.format(measure_target.__name__, (time2-time1) ))
print('{:s} took {:.9f} ms to run'.format(measure_target.__name__, (time2-time1)*1e3 ))
print('{:s} took {:.9f} μs to run'.format(measure_target.__name__, (time2-time1)*1e6 ))



### Reference from Python official document
# https://docs.python.org/3/library/time.html

##      time.perf_counter() → float

# Return the value (in fractional seconds) of a performance counter, 
# i.e. a clock with the highest available resolution to measure a short duration. 

# It does include time elapsed during sleep and is system-wide. 

# The reference point of the returned value is undefined, 
# so that only the difference between the results of consecutive calls is valid.



##      time.sleep(secs)

# Suspend execution of the calling thread for the given number of seconds. 
# The argument may be a floating point number to indicate a more precise sleep time. 
# The actual suspension time may be less than that requested 
# because any caught signal will terminate the sleep() following execution of that signal’s catching routine. 

# Also, the suspension time may be longer than requested by an arbitrary amount 
# because of the scheduling of other activity in the system.

