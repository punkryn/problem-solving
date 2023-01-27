# https://www.acmicpc.net/problem/6118
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
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = mis()
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque([1])
    v = [INF] * (n + 1)
    v[1] = 0

    while q:
        x = q.popleft()

        for nxt in graph[x]:
            if v[nxt] != INF:
                continue

            v[nxt] = v[x] + 1
            q.append(nxt)
    
    d = 0
    for i in range(1, n + 1):
        if v[i] == INF:
            continue
        d = max(d, v[i])
    
    print(f'{v.index(d)} {d} {v.count(d)}')