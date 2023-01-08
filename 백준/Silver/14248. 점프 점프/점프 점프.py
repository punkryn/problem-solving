# https://www.acmicpc.net/problem/14248
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    A = [0] + list(mis())
    s = int(si())

    q = deque([s])
    v = set([s])

    while q:
        cur = q.popleft()

        for d in [A[cur], -A[cur]]:
            nxt = cur + d
            if not (1 <= nxt <= n):
                continue
            if nxt in v:
                continue
            
            v.add(nxt)
            q.append(nxt)
    print(len(v))