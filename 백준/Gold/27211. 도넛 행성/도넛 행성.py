import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y):
    q = deque([(x, y)])
    v[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = (x + dx[i]) % n
            ny = (y + dy[i]) % m

            if v[nx][ny]: continue
            if planet[nx][ny] == 1:
                continue
            
            v[nx][ny] = 1
            q.append((nx, ny))
            

if __name__ == '__main__':
    n, m = mis()
    planet = [list(mis()) for _ in range(n)]

    ans = 0
    v = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if planet[i][j] == 1:
                continue

            if v[i][j]: continue

            BFS(i, j)
            ans += 1
    print(ans)