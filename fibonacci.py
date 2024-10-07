# the first way to do it is to step through a For loop
#def fibonacci(n):
#    if n < 1:
#        return None
# there is no Fibonacci of 0
#    if n < 3:
#        return 1
# the first two Fibonacci numbers are both 1 (i.e. 1, 1, 2, 3...)
#    elem_1 = elem_2 = 1
#    the_sum = 0
# setting initial values for the For loop
#    for i in range(3, n + 1):
#        the_sum = elem_1 + elem_2
#        elem_1, elem_2 = elem_2, the_sum
#    return the_sum
#
#for n in range(1, 10):
#    print(n, "->", fibonacci(n))

# but perhaps a more intuitive way would be to use recursion

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

# think through the recursion... make sure you catch all the things that could
# cause it to loop forever and ever and ever 
