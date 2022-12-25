# https://www.acmicpc.net/problem/2553
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())

    ans = 1
    for i in range(1, n + 1):
        ans *= i
        ans %= 100_000_000
        while ans % 10 == 0:
            ans //= 10
    
    print(ans % 10)