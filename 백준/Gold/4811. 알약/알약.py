# https://www.acmicpc.net/problem/4811
import sys
import math
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    dp = [[0] * 31 for _ in range(60)]
    dp[1][1] = 1
    dp[2][1] = 1; dp[2][2] = 1
    for i in range(3, 60):
        for j in range(math.ceil(i / 2), 31):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    while True:
        x = int(si())
        if x == 0:
            break

        print(dp[x + x - 1][x])