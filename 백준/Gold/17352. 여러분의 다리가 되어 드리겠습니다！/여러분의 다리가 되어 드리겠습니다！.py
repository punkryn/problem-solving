# https://www.acmicpc.net/problem/17352
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

if __name__ == '__main__':
    n = int(si())
    parent = [i for i in range(n + 1)]

    for _ in range(n - 2):
        a, b = mis()
        if find_parent(a) != find_parent(b):
            union(a, b)
    
    f = find_parent(1)
    for i in range(2, n + 1):
        if f != find_parent(i):
            print(1, i)
            break