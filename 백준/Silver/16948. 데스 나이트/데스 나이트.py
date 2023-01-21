# https://www.acmicpc.net/problem/16948
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

if __name__ == '__main__':
    n = int(si())
    r1, c1, r2, c2 = mis()

    ans = -1
    q = deque([(r1, c1)])
    v = [[-1] * n for _ in range(n)]
    v[r1][c1] = 0

    while q:
        r, c = q.popleft()

        if r == r2 and c == c2:
            ans = v[r][c]
            break

        for i in range(6):
            nr = r + dx[i]
            nc = c + dy[i]

            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if v[nr][nc] != -1:
                continue
            v[nr][nc] = v[r][c] + 1
            q.append((nr, nc))
    print(ans)