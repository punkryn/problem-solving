# https://www.acmicpc.net/problem/13913
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, k = mis()

    q = deque([(n, 0)])
    v = [-1] * 200_001
    v[n] = -2

    while q:
        cur, time = q.popleft()

        if cur == k:
            print(time)
            break

        for nxt in [cur - 1, cur + 1, cur * 2]:
            if not (0 <= nxt <= 200_000):
                continue
            if v[nxt] != -1:
                continue

            v[nxt] = cur
            q.append((nxt, time + 1))
    
    path = [k]
    cur = k
    while v[cur] != -2:
        path.append(v[cur])
        cur = v[cur]
    print(*path[::-1])