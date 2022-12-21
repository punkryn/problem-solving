# https://www.acmicpc.net/problem/2211
import sys
from heapq import heappush, heappop
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
        a, b, c = mis()
        graph[a].append((b, c))
        graph[b].append((a, c))
    q = [(0, 1)]
    prev = [-1] * (n + 1)
    dist = [INF] * (n + 1)
    dist[1] = 0

    while q:
        cur_cost, cur = heappop(q)

        if cur_cost != dist[cur]:
            continue

        for nxt, cost in graph[cur]:
            nxt_cost = cost + cur_cost
            if nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                heappush(q, (nxt_cost, nxt))
                prev[nxt] = cur
    
    ans = set()
    for i in range(2, n + 1):
        cur = i
        while prev[cur] != -1:
            if (cur, prev[cur]) not in ans and (prev[cur], cur) not in ans:
                ans.add((cur, prev[cur]))
            cur = prev[cur]
    print(len(ans))
    for edge in ans:
        print(*edge)