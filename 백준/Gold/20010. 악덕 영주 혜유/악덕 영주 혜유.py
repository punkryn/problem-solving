# https://www.acmicpc.net/problem/20010
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def dfs(x, prev, cost):
    global max_cost, root

    if max_cost < cost:
        max_cost = cost
        root = x
    
    for nxt, ncost in graph[x]:
        if nxt == prev:
            continue
        dfs(nxt, x, cost + ncost)

if __name__ == '__main__':
    n, k = mis()

    parent = [i for i in range(n)]
    edges = sorted([list(mis()) for _ in range(k)], key=lambda x: x[2])

    graph = [[] for _ in range(n)]
    min_cost = 0
    for a, b, c in edges:
        if find_parent(a) != find_parent(b):
            union(a, b)
            min_cost += c

            graph[a].append((b, c))
            graph[b].append((a, c))
    
    max_cost = 0
    root = 0
    dfs(root, -1, 0)
    dfs(root, -1, 0)
    print(min_cost)
    print(max_cost)