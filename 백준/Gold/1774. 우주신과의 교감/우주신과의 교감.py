# https://www.acmicpc.net/problem/1774
import sys
si = sys.stdin.readline

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
    n, m = map(int, si().split())
    coord = [[0, 0]] + [list(map(int, si().split())) for _ in range(n)]
    edges = sorted([(((coord[i][0] - coord[j][0]) ** 2 + (coord[i][1] - coord[j][1]) ** 2) ** 0.5, i, j) for i in range(1, n) for j in range(2, n + 1) if i != j])
    parent = [i for i in range(n + 1)]
    
    connected = set()
    for _ in range(m):
        x, y = map(int, si().split())
        connected.add((x, y))
        union(x, y)

    ans = 0
    for cost, x, y in edges:
        if (x, y) in connected: continue
        if find_parent(x) != find_parent(y):
            union(x, y)
            ans += cost
    print(f'{ans:.2f}')