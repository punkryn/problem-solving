# https://www.acmicpc.net/problem/26009
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def oob(x, y):
    if not (1 <= x <= n and 1 <= y <= m):
        return True
    return False

if __name__ == '__main__':
    n, m = mis()
    k = int(si())
    
    grid = [[-1] * (m + 1) for _ in range(n + 1)]
    for _ in range(k):
        r, c, d = mis()
        grid[r][c] = -2
        for i in range(d + 1):
            nr = r - i + d
            nc = c - i
            if oob(nr, nc): continue
            grid[nr][nc] = -2
        
        for i in range(d + 1):
            nr = r - i + d
            nc = c + i
            if oob(nr, nc): continue
            grid[nr][nc] = -2
        
        for i in range(d + 1):
            nr = r + i - d
            nc = c - i
            if oob(nr, nc): continue
            grid[nr][nc] = -2
        
        for i in range(d + 1):
            nr = r + i - d
            nc = c + i
            if oob(nr, nc): continue
            grid[nr][nc] = -2
    
    q = deque([(1, 1)])
    grid[1][1] = 0

    while q:
        x, y = q.popleft()

        if x == n and y == m:
            break
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if oob(nx, ny): continue
            if grid[nx][ny] != -1: continue

            grid[nx][ny] = grid[x][y] + 1
            q.append((nx, ny))
    
    if grid[n][m] == -1:
        print('NO')
    else:
        print('YES')
        print(grid[n][m])