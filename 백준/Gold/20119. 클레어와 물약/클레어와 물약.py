# https://www.acmicpc.net/problem/20119
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

if __name__ == '__main__':
    n, m = mis()

    graph = [[] for _ in range(n + 1)]
    edges = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        rec = list(mis())
        
        k = rec[0]
        req = rec[1: k + 1]
        res = rec[-1]

        graph[res].append(set(rec[1: k + 1]))
        
        for x in req:
            edges[x].append(res)
    
    L = int(si())
    ans = set([*list(mis())])
    q = deque()

    for a in ans:
        q.append(a)
    
    while q:
        cur = q.popleft()

        for nxt in edges[cur]:
            if nxt in ans: continue
            
            for node in graph[nxt]:
                if cur in node:
                    node.remove(cur)

            for node in graph[nxt]:
                if len(node) == 0:
                    q.append(nxt)
                    ans.add(nxt)
                    break
    print(len(ans))
    print(*sorted(ans))