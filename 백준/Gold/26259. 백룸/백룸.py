# https://www.acmicpc.net/problem/26259
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = mis()

    room = [list(mis()) for _ in range(n)]
    wall = list(mis())
    
    x1, y1, x2, y2 = wall
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    
    if y1 == 0 and y2 == m and (1 <= x1 < n):
        print('Entity')
        exit()
    
    if x1 == 0 and x2 == n and (1 <= y1 < m):
        print('Entity')
        exit()

    if x1 == x2:
        y2 -= 1
    elif y1 == y2:
        x2 -= 1

    dp = [[-INF] * m for _ in range(n)]
    dp[0][0] = room[0][0]
    for i in range(n):
        for j in range(m):
            if i - 1 >= 0 and not ((x1 == x2) and (x1 <= i <= x2 and y1 <= j <= y2)):
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + room[i][j])
            
            if j - 1 >= 0 and not ((y1 == y2) and (x1 <= i <= x2 and y1 <= j <= y2)):
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + room[i][j])
    
    print(dp[n - 1][m - 1] if dp[n - 1][m - 1] != -INF else 'Entity')