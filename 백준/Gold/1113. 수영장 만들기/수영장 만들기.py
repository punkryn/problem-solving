# https://www.acmicpc.net/problem/1113
import sys
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
si = sys.stdin.readline
mis = lambda: map(int, si().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, h_):
    global ans
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < n and 0 <= ny < m): continue
        if v[nx][ny]: continue

        if h[nx][ny] < h_:
            v[nx][ny] = 1
            ans += h_ - h[nx][ny]
            DFS(nx, ny, h_)
        else:
            v[nx][ny] = 1
            heappush(q, (h[nx][ny], nx, ny))

if __name__ == '__main__':
    n, m = mis()
    h = [list(map(int, si().strip())) for _ in range(n)]

    q = []
    v = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                heappush(q, (h[i][j], i, j))
                v[i][j] = 1
    ans = 0
    while q:
        h_, x, y = heappop(q)
        
        DFS(x, y, h_)
    print(ans)