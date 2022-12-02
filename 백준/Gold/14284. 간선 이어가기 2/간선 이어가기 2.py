# https://www.acmicpc.net/problem/14284
import sys
from heapq import heappush, heappop
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

if __name__ == '__main__':
    n, m = mis()
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = mis()
        graph[a].append((b, c))
        graph[b].append((a, c))
    s, t = mis()

    dist = [INF] * (n + 1)
    dist[s] = 0
    q = [(0, s)]
    while q:
        cur_cost, cur = heappop(q)

        if cur_cost > dist[cur]: continue

        for nxt, cost in graph[cur]:
            nxt_cost = cost + cur_cost
            if nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                heappush(q, (nxt_cost, nxt))
    
    print(dist[t])