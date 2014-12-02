# https://www.hackerrank.com/challenges/missing-numbers 

from sys import stdin
_, A_list = stdin.readline(), stdin.readline().split()
_, B_list = stdin.readline(), stdin.readline().split()

numbers_set = {}

# Add all integers from b, then remove the ones in A. The leftovers are the missing numbers.
for b in B_list:
    if b in numbers_set:
        numbers_set[b] += 1
    else:
        numbers_set[b] = 1
        
for a in A_list:
    # If it's in A it has to have been in B
    numbers_set[a] -= 1
    if numbers_set[a] == 0:
        del numbers_set[a]

results = []
for missing in sorted(numbers_set.keys()):
    results += [missing]
        

print " ".join(results)