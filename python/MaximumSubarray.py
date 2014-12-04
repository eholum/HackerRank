# https://www.hackerrank.com/challenges/maxsubarray

# Solved using Kadane's Algorithm for maximum subarrays.
from sys import stdin

def compute_max_subarray(array):
    non_contig_max = 0
    current_max = float("-inf")
    overall_max = float("-inf")
    results = []
    
    for i in xrange(len(array)):
        if array[i] > 0:
            non_contig_max += array[i]
            
        # Doesn't help us if the sum at this point is negative
        if current_max < 0:
            current_max = array[i]
        else:
            current_max = current_max + array[i]
        if current_max > overall_max:
            overall_max = current_max
        results.append(overall_max)
    
    # No positive values
    if overall_max < 0:
        non_contig_max = overall_max
        
    return str(overall_max) + " " + str(non_contig_max)

samples = int(stdin.readline())
for i in xrange(samples):   
   stdin.readline()
   line = map(long, stdin.readline().split(" "))
   print compute_max_subarray(array)