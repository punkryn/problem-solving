# https://www.acmicpc.net/problem/15789
import sys
from heapq import heappush, heappop
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
    n, m = mis()

    parent = [i for i in range(n + 1)]

    for _ in range(m):
        x, y = mis()
        if find_parent(x) != find_parent(y):
            union(x, y)
    
    group = dict()
    for i in range(1, n + 1):
        p = find_parent(i)
        if p not in group:
            group[p] = 0
        group[p] += 1

    c, h, k = mis()

    cGroup = find_parent(c)
    hGroup = find_parent(h)

    ans = group[cGroup]
    for key, value in sorted(group.items(), key=lambda x: x[1], reverse=True):
        if not k:
            break
        
        curGroup = find_parent(key)
        if curGroup == hGroup:
            continue

        ans += group[curGroup]
        k -= 1
    print(ans)