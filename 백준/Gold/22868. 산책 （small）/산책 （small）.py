# https://www.acmicpc.net/problem/22868
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(start, end, flag):
    q = deque([start])
    v = [INF] * (n + 1)
    v[start] = 0
    
    while q:
        x = q.popleft()

        if x == end:
            break

        for nxt in graph[x]:
            if not flag and nxt in visited:
                continue
            if v[nxt] != INF: continue
            v[nxt] = v[x] + 1
            q.append(nxt)
            if flag: prev[nxt] = x

    return v[end]

if __name__ == '__main__':
    n, m = mis()
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = mis()
        graph[a].append(b)
        graph[b].append(a)
    
    s, e = mis()

    for g in graph:
        g.sort()
    
    prev = [-1] * (n + 1)

    ans = 0
    ans += BFS(s, e, True)
    
    cur = e
    visited = set()
    while cur != s:
        nxt = prev[cur]
        visited.add(cur)

        cur = nxt
        
    ans += BFS(e, s, False)
    print(ans)