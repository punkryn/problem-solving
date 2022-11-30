# https://www.acmicpc.net/problem/22865
import sys
from heapq import heappush, heappop
si = sys.stdin.readline
mis = lambda: map(int, si().split())

INF = float('inf')

def dijkstra(x):
    dist = [INF] * (n + 1)
    q = [(0, x)]
    dist[x] = 0

    while q:
        cur_cost, cur = heappop(q)

        if cur_cost > dist[cur]:
            continue

        for nxt, cost in graph[cur]:
            nxt_cost = cur_cost + cost
            if nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                heappush(q, (nxt_cost, nxt))
    return dist

if __name__ == '__main__':
    n = int(si())
    a, b, c = mis()
    m = int(si())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        d, e, l = mis()
        graph[d].append((e, l))
        graph[e].append((d, l))
    
    adist = dijkstra(a)
    bdist = dijkstra(b)
    cdist = dijkstra(c)

    ans_dist = 0
    ans = 0
    for i in range(1, n + 1):
        tmp = min(adist[i], bdist[i], cdist[i])
        if ans_dist < tmp:
            ans_dist = tmp
            ans = i
    print(ans)