# https://www.acmicpc.net/problem/16137
import sys
from heapq import heappush, heappop
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dijkstra():
    q = [(0, 0, 0, 0)]
    v = [[INF] * n for _ in range(n)]
    v[0][0] = 0

    while q:
        t, x, y, flag = heappop(q)

        if v[x][y] < t:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if grid[nx][ny] == 0:
                continue

            if grid[nx][ny] == 1:
                nxt_time = t + 1
                if nxt_time < v[nx][ny]:
                    v[nx][ny] = nxt_time
                    heappush(q, (nxt_time, nx, ny, 0))
            else:
                if flag: continue
                MOD = (t + 1) % grid[nx][ny]
                if MOD == 0:
                    nxt_time = t + 1
                    if nxt_time < v[nx][ny]:
                        v[nx][ny] = nxt_time
                        heappush(q, (nxt_time, nx, ny, 1))
                else:
                    nxt_time = grid[nx][ny] * ((t + 1) // grid[nx][ny] + 1)
                    if nxt_time < v[nx][ny]:
                        v[nx][ny] = nxt_time
                        heappush(q, (nxt_time, nx, ny, 1))
    
    return v[n - 1][n - 1]

if __name__ == '__main__':
    n, m = mis()
    grid = [list(mis()) for _ in range(n)]

    cliff = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                cliff.append((i, j))

    ans = INF
    for x, y in cliff:
        grid[x][y] = m

        ans = min(ans, dijkstra())

        grid[x][y] = 0
    print(ans)