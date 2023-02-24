# https://www.acmicpc.net/problem/10845
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
    q = deque()
    for _ in range(n):
        op = si().strip()
        if len(op) == 3:
            if not q:
                print(-1)
            else:
                print(q.popleft())
        elif len(op) == 4:
            if op == 'size':
                print(len(q))
            else:
                if not q:
                    print(-1)
                else:
                    print(q[-1])
        elif len(op) == 5:
            if op == 'empty':
                if not q:
                    print(1)
                else:
                    print(0)
            else:
                if not q:
                    print(-1)
                else:
                    print(q[0])
        else:
            _, X = op.split()
            q.append(X)
    