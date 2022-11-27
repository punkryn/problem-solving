# https://www.acmicpc.net/problem/25189
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = float('inf')

def bfs(x, y, v, adj):
    q = deque([(x, y)])
    v[x][y] = 1

    while q:
        x, y = q.popleft()
        
        for nx, ny in adj[x][y]:
            if v[nx][ny] != INF: continue
            v[nx][ny] = v[x][y] + 1
            q.append((nx, ny))

if __name__ == '__main__':
    n, m = mis()
    rf, cf, rh, ch = mis()
    rf -= 1; cf -= 1; rh -= 1; ch -= 1
    MAP = [list(mis()) for _ in range(n)]
    adj = [[[] for _ in range(m)] for _ in range(n)]
    rev_adj = [[[] for _ in range(m)] for _ in range(n)]

    if rf == rh and cf == ch:
        print(0)
        exit()

    for i in range(n):
        for j in range(m):
            for k in range(4):
                nx = i + dx[k] * MAP[i][j]
                ny = j + dy[k] * MAP[i][j]
                if not (0 <= nx < n and 0 <= ny < m): continue
                adj[i][j].append((nx, ny))
                rev_adj[nx][ny].append((i, j))

    
    graph = [[INF] * m for _ in range(n)]
    rev_graph = [[INF] * m for _ in range(n)]
    
    bfs(rf, cf, graph, adj)
    bfs(rh, ch, rev_graph, rev_adj)


    ans = INF
    for i in range(n):
        x1 = y1 = INF
        for j in range(m):
            x1 = min(x1, graph[i][j])
            y1 = min(y1, rev_graph[i][j])
        ans = min(ans, x1 + y1 - 1)
    
    for j in range(m):
        x1 = y1 = INF
        for i in range(n):
            x1 = min(x1, graph[i][j])
            y1 = min(y1, rev_graph[i][j])
        ans = min(ans, x1 + y1 - 1)
    print(ans if ans != INF else -1)