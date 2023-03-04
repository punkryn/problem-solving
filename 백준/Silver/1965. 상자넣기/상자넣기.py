# https://www.acmicpc.net/problem/1965
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    B = list(mis())
    
    dp = [1] * n
    ans = 0
    for i in range(1, n):
        for j in range(i):
            if B[j] < B[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        ans = max(ans, dp[i])
    print(ans)