# https://www.acmicpc.net/problem/5926
import sys
from collections import defaultdict
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    cows = sorted([tuple(mis()) for _ in range(n)])
    
    length = len(set([x[1] for x in cows]))

    l = 0; r = 1
    ans = INF
    cand = defaultdict(int)

    cand[cows[0][1]] += 1
    while r < n:
        while cand[cows[l][1]] > 1:
            cand[cows[l][1]] -= 1

            if cand[cows[l][1]] == 0:
                del cand[cows[l][1]]
            
            l += 1
        
        if length == len(cand):
            ans = min(ans, cows[r - 1][0] - cows[l][0])
        
        cand[cows[r][1]] += 1
        r += 1
    
    while cand[cows[l][1]] > 1:
        cand[cows[l][1]] -= 1

        l += 1

    if length == len(cand):
        ans = min(ans, cows[r - 1][0] - cows[l][0])
    
    print(ans)