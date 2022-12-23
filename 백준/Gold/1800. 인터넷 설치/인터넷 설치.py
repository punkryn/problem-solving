# https://www.acmicpc.net/problem/1800
import sys
from collections import deque, defaultdict
from heapq import heappush, heappop
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def deter(mid):
    q = [(0, 1, 0)]
    v = [[INF] * (k + 1) for _ in range(n + 1)]
    v[1][0] = 0
    
    while q:
        cur_cost, cur, cur_cnt = heappop(q)

        if v[cur][cur_cnt] < cur_cost:
            continue

        for nxt, cost in graph[cur]:
            if cost > mid:
                nxt_cnt = cur_cnt + 1
                if nxt_cnt > k: continue
                nxt_cost = cur_cost + 0
                if v[nxt][nxt_cnt] > nxt_cost:
                    v[nxt][nxt_cnt] = nxt_cost
                    heappush(q, (nxt_cost, nxt, nxt_cnt))
            else:
                nxt_cnt = cur_cnt + 1
                nxt_cost = cur_cost + 0
                if nxt_cnt <= k and v[nxt][nxt_cnt] > nxt_cost:
                    v[nxt][nxt_cnt] = nxt_cost
                    heappush(q, (nxt_cost, nxt, nxt_cnt))
                
                nxt_cnt = cur_cnt
                nxt_cost = cur_cost + cost
                if nxt_cnt > k: continue
                if v[nxt][nxt_cnt] > nxt_cost:
                    v[nxt][nxt_cnt] = nxt_cost
                    heappush(q, (nxt_cost, nxt, nxt_cnt))
    return min(v[n]) != INF
                

if __name__ == '__main__':
    n, p, k = mis()
    graph = [[] for _ in range(n + 1)]
    for _ in range(p):
        a, b, c = mis()
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    if n == 1:
        print(0)
        exit()

    l, r = 0, 1_000_000
    ans = -1

    while l <= r:
        mid = (l + r) // 2

        if deter(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)