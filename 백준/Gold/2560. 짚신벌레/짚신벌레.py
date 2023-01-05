# https://www.acmicpc.net/problem/2560
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

MOD = 1000

if __name__ == '__main__':
    a, b, d, n = mis()

    dp = [0] * (n + 1)
    dp[0] = 1

    ans = 1
    SUM = 0
    for i in range(1, n + 1):
        if i - a >= 0:
            SUM = (SUM + dp[i - a]) % MOD
        if i - b >= 0:
            SUM = (SUM - dp[i - b]) % MOD
        dp[i] = SUM

        ans += dp[i]
        if i - d >= 0:
            ans = (ans - dp[i - d]) % MOD
    
    print(ans % MOD)