# https://www.acmicpc.net/problem/13418
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

UP = 0
DOWN = 1

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    parent[y] = x

if __name__ == '__main__':
    n, m = mis()
    edges = []
    for _ in range(m + 1):
        a, b, c = mis()
        edges.append((c, a, b))
        edges.append((c, b, a))
    
    edges = sorted(edges)
    parent = [i for i in range(n + 1)]    
    
    cnt1 = 0
    for TYPE, x, y in edges:
        if find_parent(x) != find_parent(y):
            union(x, y)
            if TYPE == UP:
                cnt1 += 1
    
    parent = [i for i in range(n + 1)]
    cnt2 = 0
    for TYPE, x, y in edges[::-1]:
        if find_parent(x) != find_parent(y):
            union(x, y)
            if TYPE == UP:
                cnt2 += 1
    print(cnt1 ** 2 - cnt2 ** 2)