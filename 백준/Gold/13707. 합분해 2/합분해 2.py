# https://www.acmicpc.net/problem/13707
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

MOD = 10**9

if __name__ == '__main__':
    n, k = mis()

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, k + 1):
        dp[1][i] = i

    for i in range(2, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
    print(dp[n][k] % MOD)