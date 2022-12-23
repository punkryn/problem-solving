# https://www.acmicpc.net/problem/20209
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
    A = [0] + list(mis())
    switch = [0] + [list(mis()) for _ in range(k)]

    q = deque([(0, A[:])])
    v = set([tuple(A[1:])])
    while q:
        cnt, state = q.popleft()

        if len(set(state[1:])) == 1:
            print(cnt)
            exit()

        for i in range(1, k + 1):
            tmp = state[:]
            for nxt in switch[i][1:]:
                tmp[nxt] = (tmp[nxt] + i) % 5
            
            if tuple(tmp[1:]) in v: continue
            
            q.append((cnt + 1, tmp[:]))
            v.add(tuple(tmp[1:]))
    print(-1)