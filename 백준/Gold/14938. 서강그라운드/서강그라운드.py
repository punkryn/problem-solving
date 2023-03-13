# https://www.acmicpc.net/problem/14938
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, prev, length):
    ret = t[x]
    for nxt, l in graph[x]:
        if nxt == prev:
            continue

        if v[nxt]: continue
        if length + l > m: continue

        v[nxt] = True
        if not s[nxt]:
            s[nxt] = True
            ret += DFS(nxt, x, length + l)
        else:
            ret += DFS(nxt, x, length + l) - t[nxt]
        v[nxt] = False
    return ret


if __name__ == '__main__':
    n, m, r = mis()
    t = [0] + list(mis())
    graph = [[] for _ in range(n + 1)]
    for _ in range(r):
        a, b, l = mis()
        graph[a].append((b, l))
        graph[b].append((a, l))
    
    
    ans = 0
    for i in range(1, n + 1):
        v = [False] * (n + 1)
        s = [False] * (n + 1)
        v[i] = True
        s[i] = True
        ans = max(ans, DFS(i, 0, 0))
    print(ans)