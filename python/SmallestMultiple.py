# https://www.hackerrank.com/contests/projecteuler/challenges/euler005

# LCM(1, 2, ..., N) =  the product of primes and the greatest power less than or 
# equal to N. Since we're only interested up to N = 40, that makes things relatively simple.
from math import log, pow
from sys import stdin

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
def compute_lcm(N):
    lcm = 1L
    
    for i in primes:
        exponent = int(log(N, i))
        lcm *= pow(i, exponent)
        
    return int(lcm)
        
samples = int(stdin.readline())

for i in xrange(samples):
   print compute_lcm(float(stdin.readline()))