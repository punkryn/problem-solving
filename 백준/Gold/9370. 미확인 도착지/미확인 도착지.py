# https://www.acmicpc.net/problem/9370
import sys
from heapq import heappush, heappop
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dijkstra(x):
    dist = [INF] * (n + 1)
    q = [(0, x)]
    dist[x] = 0

    while q:
        cur_dist, cur = heappop(q)

        if cur_dist > dist[cur]: continue

        for nxt, cost in graph[cur]:
            nxt_cost = cur_dist + cost
            if dist[nxt] > nxt_cost:
                dist[nxt] = nxt_cost
                heappush(q, (nxt_cost, nxt))
    return dist

if __name__ == '__main__':
    for _ in range(int(si())):
        n, m, t = mis()

        s, g, h = mis()

        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            a, b, d = mis()
            if (a == g and b == h) or (a == h and b == g):
                smell = d
            graph[a].append((b, d))
            graph[b].append((a, d))
        
        candidate = [int(si()) for _ in range(t)]
        ans = []
        dist = dijkstra(s)
        
        # s -> g -> h -> e
        dist_h = dijkstra(h)
        for cand in candidate:
            if dist[cand] == INF: continue
            if dist[g] + smell + dist_h[cand] == dist[cand]:
                ans.append(cand)

        # s -> h -> g -> e
        dist_s = dijkstra(g)
        for cand in candidate:
            if dist[cand] == INF: continue
            if dist[h] + smell + dist_s[cand] == dist[cand]:
                ans.append(cand)
        
        print(*sorted(ans))