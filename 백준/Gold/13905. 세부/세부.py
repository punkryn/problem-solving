# https://www.acmicpc.net/problem/13905
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def deter(mid):
    q = deque([(s)])
    v = [False] * (n + 1)
    v[s] = True

    while q:
        x = q.popleft()

        if x == e:
            return True

        for nxt, k in graph[x]:
            if v[nxt]: continue
            if k < mid: continue
            
            v[nxt] = True
            q.append(nxt)
    return False

if __name__ == '__main__':
    n, m = mis()
    s, e = mis()
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        h1, h2, k = mis()
        graph[h1].append((h2, k))
        graph[h2].append((h1, k))
    
    l, r = 1, 1_000_000
    ans = 0
    while l <= r:
        mid = (l + r) // 2

        if deter(mid):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    print(ans)