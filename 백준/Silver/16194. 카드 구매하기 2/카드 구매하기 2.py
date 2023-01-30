# https://www.acmicpc.net/problem/16194
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    dp = [0] + list(mis())

    for i in range(1, n + 1):
        for j in range(i // 2 + 1):
            dp[i] = min(dp[i], dp[j] + dp[i - j])
    print(dp[n])