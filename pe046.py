#Problem 16 from Euler Project
#Goldbach's other conjecture
#
#Done in class



from sieve_eratosthenes_0 import primes_below

def satisfy_conjecture(n):
    for i in range(1, n):
        if n - 2*i*i in primes:
            return True
    return False

primes = primes_below(10000)
for n in range(3, 10000, 2):
    if n not in primes and not satisfy_conjecture(n):
        break
print(n)
