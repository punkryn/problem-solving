# https://www.acmicpc.net/problem/25953
import sys
from heapq import heappush, heappop
sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, t, m = mis()
    s, e = mis()
    graph = [[] for _ in range(n)]

    for i in range(t):
        for j in range(m):
            a, b, w = mis()
            graph[a].append((b, w, i + 1))
            graph[b].append((a, w, i + 1))
    
    dist = [[float('inf')] * n for _ in range(t + 1)]
    dist[0][s] = 0
    q = [(0, 0, s)]
    ans = float('inf')
    while q:
        cur_dist, cur_time, cur = heappop(q)

        if cur == e:
            ans = min(ans, cur_dist)
            break
        
        if cur_dist > dist[cur_time][cur]: continue

        for nxt, cost, time in graph[cur]:
            if time <= cur_time: continue
            nxt_dist = cur_dist + cost
            if nxt_dist < dist[time][nxt]:
                dist[time][nxt] = nxt_dist
                heappush(q, (nxt_dist, time, nxt))
    
    print(ans if ans != float('inf') else -1)