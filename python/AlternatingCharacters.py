# https://www.hackerrank.com/challenges/alternating-characters
def process(word):
    i = 0
    count = 0
    for i in xrange(len(word)-1):
        if (word[i] == word[i+1]):
            count += 1
    return count

from sys import stdin
lines = int(stdin.readline())

for i in xrange(lines):
    print str(process(stdin.readline()))