# https://www.acmicpc.net/problem/17499
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, q = mis()
    A = deque(mis())

    state = 0
    for _ in range(q):
        op, *args = mis()
        
        if op == 1:
            idx, x = args
            idx -= 1

            idx = (idx - state) % n
            A[idx] += x
        elif op == 2:
            s = args[0]
            state += s
        else:
            s = args[0]
            state -= s
    
    if state > 0:
        state %= n
        for _ in range(state):
            A.appendleft(A.pop())
    elif state < 0:
        state %= n
        for _ in range(n - state):
            A.append(A.popleft())
            
    print(*A)