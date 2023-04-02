# https://www.acmicpc.net/problem/3151
import sys
from bisect import bisect_left, bisect_right
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    A = sorted(mis())

    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            SUM = A[i] + A[j]
            l = bisect_left(A, -SUM, j + 1, n)
            u = bisect_right(A, -SUM, j + 1, n)
            ans += u - l
    print(ans)