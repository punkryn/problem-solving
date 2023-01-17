# https://www.acmicpc.net/problem/11780
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si()); m = int(si())
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 0
    
    for _ in range(m):
        a, b, c = mis()
        dp[a][b] = min(dp[a][b], c)
    
    routes = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j: continue

                nxt = dp[i][k] + dp[k][j]
                if nxt < dp[i][j]:
                    dp[i][j] = nxt
                    routes[i][j] = routes[i][k][:] + [k] + routes[k][j][:]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(dp[i][j] if dp[i][j] != INF else 0, end=' ')
        print()
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j or dp[i][j] == INF:
                print(0)
                continue

            print(2 + len(routes[i][j]), end=' ')
            print(i, *routes[i][j], j)