# https://www.acmicpc.net/problem/10159
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

if __name__ == '__main__':
    n = int(si())
    m = int(si())
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][i] = 1
    
    for _ in range(m):
        a, b = mis()
        dp[a][b] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dp[i][k] and dp[k][j]:
                    dp[i][j] = 1
    
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if not dp[i][j] and not dp[j][i]:
                cnt += 1
        print(cnt)