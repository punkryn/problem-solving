# https://www.acmicpc.net/problem/10282
import sys
from heapq import heappush, heappop
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

if __name__ == '__main__':
    for _ in range(int(si())):
        n, d, c = mis()
        graph = [[] for _ in range(n + 1)]
        for _ in range(d):
            a, b, s = mis()
            graph[b].append((a, s))
        
        q = [(0, c)]
        dist = [INF] * (n + 1)
        dist[c] = 0

        while q:
            cur_time, cur = heappop(q)
            
            if dist[cur] < cur_time: continue

            for nxt, time in graph[cur]:
                nxt_time = cur_time + time
                if nxt_time < dist[nxt]:
                    dist[nxt] = nxt_time
                    heappush(q, (nxt_time, nxt))
        ans = 0
        cnt = 0
        for i in range(1, n + 1):
            if dist[i] == INF: continue
            cnt += 1
            ans = max(ans, dist[i])
        print(cnt, ans)