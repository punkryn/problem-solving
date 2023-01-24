# https://www.acmicpc.net/problem/15806
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

if __name__ == '__main__':
    n, m, k, t = mis()
    q = deque()
    v = [[[False] * 2 for _ in range(n + 1)] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = mis()
        q.append((a, b, 0))
        v[a][b][0] = True
    
    flag = True
    while q:
        x, y, d = q.popleft()

        if d >= t:
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = (d + 1) % 2

            if not (1 <= nx <= n and 1 <= ny <= n):
                continue
            
            if v[nx][ny][nd]:
                continue

            v[nx][ny][nd] = True
            q.append((nx, ny, d + 1))
            flag = False

    d = t % 2
    ans = False
    for _ in range(k):
        a, b = mis()

        ans |= v[a][b][d]

    if flag:
        print('NO')
    else:
        print('YES' if ans else 'NO')