# https://www.acmicpc.net/problem/14929
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    A = list(mis())
    SUM = 0
    ans = 0
    for i in range(1, n):
        SUM += A[i - 1]
        ans += SUM * A[i]
    print(ans)