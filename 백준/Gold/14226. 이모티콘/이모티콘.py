# https://www.acmicpc.net/problem/14226
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    s = int(si())

    v = set([(1, 0, 0)])
    q = deque([(1, 0, 0)])

    ans = 0
    while q:
        cnt, t, clip = q.popleft()

        if cnt == s:
            ans = t
            break

        nxt = (cnt, t + 1, cnt)
        if nxt not in v:
            v.add(nxt)
            q.append(nxt)
        
        nxt = (cnt + clip, t + 1, clip)
        if clip and nxt not in v:
            v.add(nxt)
            q.append(nxt)
        
        nxt = (cnt - 1, t + 1, clip)
        if cnt and nxt not in v:
            v.add(nxt)
            q.append(nxt)
    
    print(ans)