# https://www.hackerrank.com/challenges/sherlock-and-queries

# See the javascript implementation to understand why python is better.
from sys import stdin

def compute(n, m, a, b, c):
    mod = 1000000007
    b_counts = {}
    
    for i in range(0, m):
        if b[i] in b_counts:
            b_counts[b[i]] = (b_counts[b[i]] * c[i]) % mod
        else:
            b_counts[b[i]] = c[i]
        
    for i, factor in b_counts.iteritems():
        for j in range(i - 1, n, i):
            a[j] = (a[j] * factor) % mod
    return a

[n, m] = [int(x) for x in stdin.readline().split()]
a = [int(x) for x in stdin.readline().split()]
b = [int(x) for x in stdin.readline().split()]
c = [int(x) for x in stdin.readline().split()]

print ' '.join(map(str, compute(n, m, a, b, c)))