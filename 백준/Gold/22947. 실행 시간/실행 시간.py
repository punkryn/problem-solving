# https://www.acmicpc.net/problem/22947
import sys
from collections import deque
from itertools import combinations
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

def go(times_, idg):
    q = deque([1])
    v = [0] * (n + 1)
    v[1] = times_[1]

    cand = 0
    last = 1
    while q:
        cur = q.popleft()
        last = cur
        cand = max(cand, v[cur])

        for nxt in graph[cur]:
            idg[nxt] -= 1
            v[nxt] = max(v[nxt], v[cur] + times_[nxt])

            if idg[nxt] == 0:
                q.append(nxt)
    return cand, last

if __name__ == '__main__':
    n, m, k = mis()
    times = [0] + list(mis())

    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        s, e = mis()
        indegree[e] += 1
        graph[s].append(e)
    
    times_ = times[:]
    idg = indegree[:]
    _, last = go(times_, idg)

    ans = INF
    for comb in combinations(range(2, n + 1), k):
        if last in comb: continue
        idg = indegree[:]
        times_ = times[:]
        for c in comb:
            times_[c] = 0

        cand, _ = go(times_, idg)
        
        ans = min(ans, cand)
    print(ans)