# https://www.hackerrank.com/contests/projecteuler/challenges/euler001

# Note that the sum of all multiples of 3 and 5 is equal to the sum of multiples of
# 3 plus the sum of the multiples of 5 minus the duplicates. So
# SUM = 3 * \sum(1,N/5,i) + 5 * \sum(1,N/5) - 15 * \sum(1,N/15,i)
def clever_solve(n):
    n_3 = 3 * compute_sum(floor(n,3))
    n_5 = 5 * compute_sum(floor(n,5))
    n_15 = 15 * compute_sum(floor(n,15))
    
    return n_3 + n_5 - n_15
    
def compute_sum(n):
    return (n * (n+1)) / 2
    
def floor(n,x):
    if (n % x == 0):
        return n/x - 1
    else:
        return long(n/x)

# Including this for kicks and giggles.
def brute_force_solve(n):
    total = 0
    for i in xrange(n):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i
    
    return total
    
from sys import stdin
samples = int(stdin.readline())

for i in xrange(samples):
   print clever_solve(long(stdin.readline()))