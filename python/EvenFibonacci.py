# https://www.hackerrank.com/contests/projecteuler/challenges/euler002
def compute_sum(n):
    total = 0L
    fib_a = 1L
    fib_b = 1L
    
    while fib_a < n:
        fib_c = fib_a + fib_b
        if fib_c % 2 == 0:
            total += fib_c
        fib_b = fib_a
        fib_a = fib_c
        
    print fib_c
    return total

from sys import stdin
samples = int(stdin.readline())

for i in xrange(samples):
   print compute_sum(long(stdin.readline()))