# https://www.acmicpc.net/problem/16174
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    MAP = [list(mis()) for _ in range(n)]

    q = deque([(0, 0)])
    v = [[False] * n for _ in range(n)]
    v[0][0] = True

    while q:
        x, y = q.popleft()

        if x == n - 1 and y == n - 1:
            print('HaruHaru')
            exit()

        for i in range(1, 3):
            nx = x + dx[i] * MAP[x][y]
            ny = y + dy[i] * MAP[x][y]

            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if v[nx][ny]:
                continue
            v[nx][ny] = True
            q.append((nx, ny))
    
    print('Hing')