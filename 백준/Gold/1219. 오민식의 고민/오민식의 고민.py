# https://www.acmicpc.net/problem/1219
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bf():
    global cycle
    dist = [INF] * n
    dist[s] = -city[s]

    for _ in range(n - 1):
        for i in range(n):
            for nxt, cost in graph[i]:
                nxt_cost = cost - city[nxt] + dist[i]
                if nxt_cost < dist[nxt]:
                    dist[nxt] = nxt_cost
    
    for i in range(n):
        for nxt, cost in graph[i]:
            nxt_cost = cost - city[nxt] + dist[i]
            if nxt_cost < dist[nxt]:
                cycle.append(nxt)
    
    return dist[e]

def isConnected():
    v = [False] * n
    while cycle:
        top = cycle.pop()

        for nxt, cost in graph[top]:
            if v[nxt]: continue
            v[nxt] = True
            cycle.append(nxt)

    return v[e]

if __name__ == '__main__':
    n, s, e, m = mis()
    graph = [[] for _ in range(n)]

    for _ in range(m):
        s_, e_, cost = mis()
        graph[s_].append((e_, cost))
    
    city = list(mis())
    cycle = []

    res = bf()
    
    if res == INF:
        print('gg')
    else:
        if isConnected():
            print('Gee')
            exit()
        
        print(-res)
