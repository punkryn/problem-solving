# https://www.acmicpc.net/problem/13549
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, k = mis()

    q = deque([n])
    v = [-1] * 100001
    v[n] = 0

    while q:
        x = q.popleft()

        if x == k:
            break
        
        if x:
            nx = x * 2
            if nx <= 100000 and v[nx] == -1:
                v[nx] = v[x]
                q.appendleft(nx)
        
        nx = x + 1
        if nx <= 100000 and v[nx] == -1:
            v[nx] = v[x] + 1
            q.append(nx)
        
        nx = x - 1
        if nx >= 0 and v[nx] == -1:
            v[nx] = v[x] + 1
            q.append(nx)
    print(v[k])