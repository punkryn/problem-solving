# https://www.acmicpc.net/problem/19238
import sys
from collections import deque
from heapq import heappush, heappop
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    v = [[-1] * n for _ in range(n)]
    v[x][y] = 0
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n): continue
            if MAP[nx][ny] == 1: continue
            if v[nx][ny] != -1: continue
            
            v[nx][ny] = v[x][y] + 1
            q.append((nx, ny))
    
    return v

if __name__ == '__main__':
    n, m, k = mis()
    MAP = [list(mis()) for _ in range(n)]

    sr, sc = mis()
    sr -= 1; sc -= 1

    infos = set()
    for _ in range(m):
        a, b, c, d = mis()
        infos.add((a - 1, b - 1, c - 1, d - 1))
    
    x, y = sr, sc
    for _ in range(m):
        v = bfs(x, y)

        cand = []
        for a, b, c, d in infos:
            if v[a][b] == -1:
                print(-1)
                exit()
            heappush(cand, (v[a][b], a, b, c, d))
        
        if not cand:
            print(-1)
            exit()
        d, sx, sy, ex, ey = heappop(cand)
        if d > k:
            print(-1)
            exit()
        
        k -= d

        v = bfs(sx, sy)
        if v[ex][ey] > k:
            print(-1)
            exit()
        
        k -= v[ex][ey]

        k += v[ex][ey] * 2
        infos.remove((sx, sy, ex, ey))
        x, y = ex, ey
        
    print(k)