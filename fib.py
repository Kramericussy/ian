'''
    For eulerproject problem 2. 
'''

def fib(a,b): 
    return a + b

def sum_up_to(maximum): 
    '''
        Return the sum of the elements of the Fibonacci sequence with even values not greater than maximum.
    '''
    a = 1
    b = 2
    total = 0 
    while a <= maximum:
        if a % 2 == 0: 
            total += a
        a, b = b, fib(a, b)
    return total

if __name__ == '__main__':
    print(sum_up_to(4e6))

    print('what?')