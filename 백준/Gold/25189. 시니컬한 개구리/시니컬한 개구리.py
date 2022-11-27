# https://www.acmicpc.net/problem/25189
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = mis()
    rf, cf, rh, ch = mis()
    rf -= 1; cf -= 1; rh -= 1; ch -= 1
    MAP = [list(mis()) for _ in range(n)]
    
    v = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
    row = [False] * n
    col = [False] * m
    
    q = deque([(rf, cf, 0)])
    v[rf][cf][0] = 0
    
    while q:
        x, y, flag = q.popleft()

        if x == rh and y == ch:
            print(v[x][y][flag])
            exit()
        
        for i in range(4):
            nx = x + dx[i] * MAP[x][y]
            ny = y + dy[i] * MAP[x][y]

            if not (0 <= nx < n and 0 <= ny < m): continue
            if v[nx][ny][flag] != -1: continue
            v[nx][ny][flag] = v[x][y][flag] + 1
            q.append((nx, ny, flag))
        
        if flag: continue
        if not row[x]:
            row[x] = True
            for i in range(m):
                if v[x][i][1] != -1: continue
                v[x][i][1] = v[x][y][0] + 1
                q.append((x, i, 1))
        if not col[y]:
            col[y] = True
            for i in range(n):
                if v[i][y][1] != -1: continue
                v[i][y][1] = v[x][y][0] + 1
                q.append((i, y, 1))
    print(-1)