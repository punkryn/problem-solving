# https://www.acmicpc.net/problem/1033
import sys
from math import gcd
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x):
    if len(graph[x]) == 1 and v[graph[x][0][0]]:
        return 1

    ret = 1
    for nxt, p, q in graph[x]:
        if v[nxt]: continue
        v[nxt] = True
        ret *= DFS(nxt) * p
    return ret

if __name__ == '__main__':
    n = int(si())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b, p, q = mis()
        graph[a].append((b, p, q))
        graph[b].append((a, q, p))
    
    ans = [1] * n
    for i in range(n):
        v = [False] * n
        v[i] = True
        tmp = 1
        for nxt, p, q in graph[i]:
            v[nxt] = True
            tmp *= DFS(nxt) * p
        ans[i] = tmp
    g = gcd(*ans)
    
    print(*map(lambda x: x // g, ans))