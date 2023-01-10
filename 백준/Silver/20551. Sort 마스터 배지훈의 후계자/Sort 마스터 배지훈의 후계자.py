# https://www.acmicpc.net/problem/20551
import sys
from bisect import bisect_left
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = mis()
    A = sorted([int(si()) for _ in range(n)])
    for _ in range(m):
        d = int(si())
        idx = bisect_left(A, d)
        if idx >= n or idx < 0 or A[idx] != d:
            print(-1)
        else:
            print(idx)