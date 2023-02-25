# https://www.acmicpc.net/problem/17490
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def find_parent(x):
    if parent[x] != x:
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
    n, m, k = mis()
    S = list(mis())
    
    edges = set([(0, 1, n), (S[n - 1], 0, n)])
    for i in range(1, n):
        edges.add((0, i, i + 1))
        edges.add((S[i - 1], 0, i))
    
    for _ in range(m):
        i, j = mis()
        if i > j:
            i, j = j, i
        edges.remove((0, i, j))
    
    if m == 0:
        print('YES')
        exit()

    parent = [i for i in range(n + 1)]

    cnt = 0
    flag = True
    for cost, x, y in sorted(edges):
        if cost != 0 and flag:
            flag = False
            prev = find_parent(1)
            for i in range(2, n + 1):
                cur = find_parent(i)
                if prev != cur:
                    break
            else:
                print('YES')
                exit()

        if find_parent(x) != find_parent(y):
            union(x, y)
            cnt += cost
        
        if cnt > k:
            print('NO')
            exit()
        
    print('YES')