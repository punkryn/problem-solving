# https://www.acmicpc.net/problem/1045
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

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

def isConnected():
    prev = find_parent(0)
    for i in range(1, n):
        cur = find_parent(i)
        if prev != cur: return False
        prev = cur
    return True

if __name__ == '__main__':
    n, m = mis()
    matrix = [si().strip() for _ in range(n)]

    parent = [i for i in range(n + 1)]
    roads = []
    ans = [0] * n
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 'Y':
                if find_parent(i) != find_parent(j):
                    union(i, j)
                    ans[i] += 1
                    ans[j] += 1
                    cnt += 1
                else:
                    roads.append((i, j))
    
    if isConnected() and m - cnt <= len(roads):
        if cnt < m:
            for i in range(m - cnt):
                ans[roads[i][0]] += 1
                ans[roads[i][1]] += 1
        print(*ans)
    else:
        print(-1)