# https://www.acmicpc.net/problem/25969
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m, k = mis()
    MAP = [list(mis()) for _ in range(n)]
    
    pattern = [list(mis()) for _ in range(5)]

    if MAP[n - 1][m - 1] == 1:
        print(-1)
        exit()
    
    pat = [(i - 2, j - 2) for i in range(5) for j in range(5) if pattern[i][j] == 1]

    q = deque([(0, 0, 0, 0)])
    v = [[[[-1] * m for _ in range(n)] for __ in range(k + 1)] for ___ in range(2)]
    v[0][0][0][0] = 0

    while q:
        x, y, cnt, flag = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m): continue
            if MAP[nx][ny] == 1: continue
            if MAP[nx][ny] == 2:
                if v[1][cnt][nx][ny] != -1: continue
                v[1][cnt][nx][ny] = v[flag][cnt][x][y] + 1
                q.append((nx, ny, cnt, 1))
            else:
                if v[flag][cnt][nx][ny] != -1: continue
                v[flag][cnt][nx][ny] = v[flag][cnt][x][y] + 1
                q.append((nx, ny, cnt, flag))
        
        if cnt == k: continue
        for ddx, ddy in pat:
            nx = x + ddx
            ny = y + ddy

            if not (0 <= nx < n and 0 <= ny < m): continue
            if MAP[nx][ny] == 1: continue
            if MAP[nx][ny] == 2:
                if v[1][cnt + 1][nx][ny] != -1: continue
                v[1][cnt + 1][nx][ny] = v[flag][cnt][x][y] + 1
                q.append((nx, ny, cnt + 1, 1))
            else:
                if v[flag][cnt + 1][nx][ny] != -1: continue
                v[flag][cnt + 1][nx][ny] = v[flag][cnt][x][y] + 1
                q.append((nx, ny, cnt + 1, flag))

    ans = float('inf')
    for i in range(k + 1):
        if v[1][i][n - 1][m - 1] == -1: continue
        ans = min(ans, v[1][i][n - 1][m - 1])
    print(ans if ans != float('inf') else -1)