import sys
def demo_range(n):

    # x iterates from 0 to (n-1)
    x = 0

    while True:

        # "yield" seems like a non-blocking "return"
        yield x
        x += 1

        if x == n :
            break


# expected output:
# 0 1 2 3 4 
for i in demo_range(5):
    print( i, end = ' ')

print()



# Demo of iterator on demo_range
# Catch end of iterator by None detection


# expected output:
# 0 1 2 3 4
# Iterator meets the end.

iteator_demo = demo_range(5)
while True:
    
    x = next(iteator_demo, None)

    if None == x:
        print("\nIterator meets the end.")
        break

    print( x, end = ' ')

print()    
# ==================================
# Demo of iterator on demo_range
# Catch end of iterator by exception handling

# expected output:
# 0 1 2 3 4
# Exception Message <class 'StopIteration'>

iteator_demo = demo_range(5)
while True:
    
    try:
        x = next(iteator_demo)
        print( x, end = ' ')

    except StopIteration as e:
        print("\nException Message", sys.exc_info()[0] )
        break
   
    
