import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m, c = mis()

    matrix = [list(mis()) for _ in range(c)]

    A = list(mis())
    B = list(mis())

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        dp[i][m - 1] = matrix[A[i] - 1][B[m - 1] - 1]

    for i in range(m):
        dp[n - 1][i] = matrix[A[n - 1] - 1][B[i] - 1]

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if i + 1 >= n or j + 1 >= m: continue
            dp[i][j] = max(dp[i][j], dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1] + matrix[A[i] - 1][B[j] - 1])
    
    dp2 = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        dp2[i][0] = matrix[A[i] - 1][B[0] - 1]
    for i in range(m):
        dp2[0][i] = matrix[A[0] - 1][B[i] - 1]
    for i in range(n):
        for j in range(m):
            dp2[i][j] = max(dp2[i][j], dp2[i - 1][j], dp2[i][j - 1], dp2[i - 1][j - 1] + matrix[A[i] - 1][B[j] - 1])
    
    print(max(max(max(row) for row in dp), max(max(row) for row in dp2)))