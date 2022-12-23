# https://www.acmicpc.net/problem/16400
import sys
from math import sqrt
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

MOD = 123_456_789

if __name__ == '__main__':
    n = int(si())

    prime = [0] * (n + 1)
    prime[1] = 1
    for i in range(2, int(sqrt(n)) + 1):
        if prime[i]: continue
        for j in range(i * i, n + 1, i):
            prime[j] = 1

    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(2, n + 1):
        if prime[i]: continue

        for j in range(i, n + 1):
            dp[j] = (dp[j] + dp[j - i]) % MOD
    print(dp[n] % MOD)