# https://www.acmicpc.net/problem/10986
import sys
from collections import defaultdict
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = mis()
    A = [0] + list(mis())

    ps = 0
    ans = 0
    hash = defaultdict(int)
    for i in range(1, n + 1):
        ps += A[i]
        
        ans += hash[ps % m]

        hash[ps % m] += 1
    
    print(ans + hash.get(0, 0))