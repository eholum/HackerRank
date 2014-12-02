# https://www.hackerrank.com/contests/projecteuler/challenges/euler006

# Using known formulae we have:
#
# (n(n+1))/2 ^ 2 - (n(n+1)(2n+1))/6
from math import pow
from sys import stdin

def sum_square_diff(n):
    sum_squared = pow(((n * (n+1))/2), 2)
    squares_sum = ((n * (n+1) * (2*n + 1)))/6
    return long(sum_squared - squares_sum)   

samples = int(stdin.readline())

for i in xrange(samples):
   print sum_square_diff(long(stdin.readline()))