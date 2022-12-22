# https://www.acmicpc.net/problem/19566
import sys
from collections import defaultdict
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, k = mis()
    A = [0] + list(mis())

    ps = [0] * (n + 1)
    hash = defaultdict(int)
    ans = 0
    for i in range(1, n + 1):
        ps[i] = ps[i - 1] + A[i]
        
        tmp = ps[i] - i * k
        ans += hash.get(tmp, 0)
        hash[tmp] += 1
    
    print(ans + hash.get(0, 0))