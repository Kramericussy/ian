'''
    For eulerproject problem 3. 
    Efficient factoring algorithms are a rich, ancient, and active area of study.  Remember this exercise!
'''
# See https://stackoverflow.com/questions/8220801/how-to-use-timeit-module/29512249 on use of timeit
import timeit


def naive(n):
    i = 2
    factors = {}
    while i < n:
        if n % i == 0:
            factors[i] = factors[i] + 1 if i in factors else 1
            n = n // i
            i = 2
        else:
            i += 1
    factors[n] = factors[n] + 1 if n in factors else 1
    return factors


if __name__ == '__main__':
    # Composite of several small factors, 2 * 3 * 5 * 6 * 71 * 23 * 17 * 101 * 51 * 9 * 77 * 1212
    composite = 21618970829905680
    # Product of the Mersenne primes 43112609 * 57885161
    mersenne_prod = 2495580313095049
    # The single large Newman-Shanks-Williams prime
    large_prime = 63018038201
    min(timeit.Timer(function).repeat)

    while True:
        x = int(input())
        print(naive(x))
