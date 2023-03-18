# https://www.acmicpc.net/problem/14567
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = mis()

    inorder = [0] * (n + 1)
    graph =[[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = mis()
        inorder[b] += 1
        graph[a].append(b)
    
    q = deque()
    v = [0] * (n + 1)
    for i in range(1, n + 1):
        if inorder[i] == 0:
            q.append(i)
            v[i] = 1
    
    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            inorder[nxt] -= 1
            if inorder[nxt] == 0:
                q.append(nxt)
                v[nxt] = v[cur] + 1
    
    print(*v[1:])