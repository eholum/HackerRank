# https://www.hackerrank.com/challenges/cavity-map
def find_cavities(depth_map):
    cavities = []
    for i in xrange(1, len(depth_map)-1):
        for j in xrange(1, len(depth_map[i])-1):
            maxi = max(depth_map[i-1][j], depth_map[i+1][j], depth_map[i][j-1], depth_map[i][j+1])
            if (maxi < depth_map[i][j]):
                cavities.append([i,j])

    for p in cavities:
        depth_map[p[0]][p[1]] = 'X'
        
    return depth_map
    
from sys import stdin

lines = int(stdin.readline())
depth_map = []
for i in xrange(lines):
    depth_map.append(list(stdin.readline().replace('\n','')))
    
results = find_cavities(depth_map)
for line in results:
    print ''.join(map(str, line))