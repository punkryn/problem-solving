# https://www.acmicpc.net/problem/16198
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(v):
    global ans
    if len(W) == 2:
        ans = max(ans, v)
        return
    
    for i in range(1, len(W) - 1):
        add = W[i - 1] * W[i + 1]
        tmp = W.pop(i)
        go(v + add)
        W.insert(i, tmp)

if __name__ == '__main__':
    n = int(si())
    W = list(mis())
    ans = 0
    go(0)
    print(ans)