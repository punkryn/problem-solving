# https://www.acmicpc.net/problem/17129
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = mis()
    MAP=[si().strip() for _ in range(n)]

    q = deque()
    v = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if MAP[i][j] == '2':
                v[i][j] = 0
                q.append((i, j))
                break
    
    while q:
        x, y = q.popleft()
        if MAP[x][y] == '3' or MAP[x][y] == '4' or MAP[x][y] == '5':
            print('TAK')
            print(v[x][y])
            exit()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if v[nx][ny] != -1:
                continue
            if MAP[nx][ny] == '1':
                continue

            v[nx][ny] = v[x][y] + 1
            q.append((nx, ny))
    
    print('NIE')