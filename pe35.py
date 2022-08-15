#Problem 35 from Euler Project
#Circular primes




from math import isqrt

def primes_below(bound):
    sieve = [True] * bound
    for i in range(2, isqrt(bound) + 1):
        if sieve[i]:
            for j in range(i*i, bound, i):
                sieve[j] = False
    result = []
    for i in range(2, len(sieve)):
        if sieve[i]:
            result += [i]
    return result

def circular_cycle(number):
    for i in range(1, len(s)):
        n = int(s[i:] + s[:i])
        if n not in PRIMES:
            return False
    return True

acc = 0
for i in range(1000000):
    if is_circular(i):
        acc += 1
print(i)