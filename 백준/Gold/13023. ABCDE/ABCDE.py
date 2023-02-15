# https://www.acmicpc.net/problem/13023
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(depth, x):
    global ans
    if depth == 4:
        print(1)
        exit()
    
    for nxt in graph[x]:
        if v[nxt]:
            continue
        
        v[nxt] = True
        go(depth + 1, nxt)
        v[nxt] = False

if __name__ == '__main__':
    n, m = mis()
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = mis()
        graph[a].append(b)
        graph[b].append(a)
    
    ans = 0
    v = [False] * n
    for i in range(n):
        v[i] = True
        go(0, i)
        v[i] = False
    print(ans)