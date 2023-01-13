# https://www.acmicpc.net/problem/16397
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, t, g = mis()
    q = deque([(n, 0)])
    v = set([n])

    ans = -1
    if n == g:
        print(0)
        exit()

    while q:
        cur, cnt = q.popleft()

        if cnt > t:
            continue

        if cur == g:
            ans = cnt
            break

        nxt = cur + 1
        if nxt > 99999:
            continue
        if nxt not in v:
            v.add(nxt)
            q.append((nxt, cnt + 1))

        if cur == 0:
            continue
        nxt = cur * 2
        if nxt > 99999:
            continue
        
        nxt = list(str(nxt))
        nxt[0] = str(int(nxt[0]) - 1)
        nxt = int(''.join(nxt))
        
        if nxt > 99999:
            continue

        if nxt not in v:
            v.add(nxt)
            q.append((nxt, cnt + 1))
    
    if ans == -1 or ans > t:
        print('ANG')
    else:
        print(ans)