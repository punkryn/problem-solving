# https://www.acmicpc.net/problem/21278
import sys
from itertools import combinations
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

if __name__ == '__main__':
    n, m = mis()
    
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = mis()
        dp[a][b] = 1
        dp[b][a] = 1
    
    for i in range(1, n + 1):
        dp[i][i] = 0
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    
    ans = INF
    c1 = c2 = 0
    for comb in combinations(range(1, n + 1), 2):
        x, y = comb
        
        total = 0
        for i in range(1, n + 1):
            total += min(dp[x][i] + dp[i][x], dp[y][i] + dp[i][y])
        
        if total < ans:
            ans = total
            c1 = x
            c2 = y

    print(c1, c2, ans)