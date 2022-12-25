# https://www.acmicpc.net/problem/12761
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    a, b, n, m = mis()

    q = deque([(0, n)])
    v = [-1] * 100_001
    v[n] = 0

    while q:
        cnt, x = q.popleft()

        for i in [a, -a, b, -b, 1, -1]:
            nx = x + i
            if not (0 <= nx <= 100_000): continue
            if v[nx] != -1: continue
            
            v[nx] = v[x] + 1
            q.append((cnt + 1, nx))
        
        for i in [a, b]:
            nx = x * i
            if not (0 <= nx <= 100_000): continue
            if v[nx] != -1: continue

            v[nx] = v[x] + 1
            q.append((cnt + 1, nx))
    
    print(v[m])