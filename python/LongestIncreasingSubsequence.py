# https://www.hackerrank.com/challenges/longest-increasing-subsequent
# Computes the longest increasing subsequence of a list
from sys import stdin

# Including this since this actually computes the sequence, but is much more memory intensive.
# The alternative only computes the lengths, but that's boring.
def compute_LIS(array):
    L = [[]] * len(array) 
    L[0] = [array[0]]
    
    for i in xrange(1, len(array)):
        for j in xrange(i):
            if (array[j] < array[i]) and (len(L[i]) < (len(L[j]) + 1)):
                # Shallow vs. deep copy
                L[i] = L[j][:]
        L[i].append(array[i])
   
    return " ".join(map(str,L[-1]))

list_length = int(stdin.readline())
array = []
for i in xrange(list_length):
    array.append(int(stdin.readline()))

print compute_LIS(array)