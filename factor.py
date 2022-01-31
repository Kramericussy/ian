'''
    For eulerproject problem 3. 
    Efficient factoring algorithms are a rich, ancient, and active area of study.  Remember this exercise!
'''


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
    while True:
        x = int(input())
        print(naive(x))
