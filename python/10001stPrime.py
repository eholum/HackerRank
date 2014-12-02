# https://www.hackerrank.com/contests/projecteuler/challenges/euler007
from sys import stdin
from math import sqrt

def nth_prime(n, primes):
    if len(primes) > n:
        return (primes, primes[n - 1])
        
    # length will double with each iteration
    numbers = range(primes[-1] + 2, primes[-1] * 2, 2)
    
    for p in primes[1:]:   
        for j in xrange(len(numbers) - 1, -1, -1):
            if numbers[j] % p == 0:
                del numbers[j]
 
    primes += numbers
    return nth_prime(n, primes)

samples = int(stdin.readline())

# easy enough to include the first primes.
primes = [2, 3]
for i in xrange(samples):
   print nth_prime(int(stdin.readline()), primes)[1]