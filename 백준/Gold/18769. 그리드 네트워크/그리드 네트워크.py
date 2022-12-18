# https://www.acmicpc.net/problem/18769
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
    for _ in range(int(si())):
        r, c = mis()
        edges = []

        for i in range(r):
            row = list(mis())

            for j in range(len(row)):
                n = i * c + j
                edges.append((row[j], n, n + 1))
        
        for i in range(r - 1):
            col = list(mis())

            for j in range(len(col)):
                n = i * c + j
                nn = (i + 1) * c + j

                edges.append((col[j], n, nn))
        
        edges.sort()

        parent = [i for i in range(r * c)]

        ans = 0
        for d, x, y in edges:
            if find_parent(x) != find_parent(y):
                union(x, y)
                ans += d
        print(ans)