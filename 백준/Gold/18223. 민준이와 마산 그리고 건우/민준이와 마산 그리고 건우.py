# https://www.acmicpc.net/problem/18223
import sys
from heapq import heappush, heappop
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

def dijkstra(x):
    dist = [INF] * (v + 1)
    q = [(0, x)]
    dist[x] = 0

    while q:
        cur_cost, cur = heappop(q)

        if cur_cost > dist[cur]: continue

        for nxt, cost in graph[cur]:
            nxt_cost = cur_cost + cost
            if dist[nxt] > nxt_cost:
                dist[nxt] = nxt_cost
                heappush(q, (nxt_cost, nxt))
    return dist

if __name__ == '__main__':
    v, e, p = mis()
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = mis()
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    dist1 = dijkstra(1)
    dist2 = dijkstra(p)
    if dist1[v] == dist1[p] + dist2[v]:
        print('SAVE HIM')
    else:
        print('GOOD BYE')