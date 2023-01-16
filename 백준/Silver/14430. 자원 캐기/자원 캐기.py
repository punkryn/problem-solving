# https://www.acmicpc.net/problem/14430
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = mis()
    MAP = [list(mis()) for _ in range(n)]

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = MAP[0][0]

    for i in range(n):
        for j in range(m):
            if i - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + MAP[i][j])
            if j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + MAP[i][j])
    print(dp[n - 1][m - 1])