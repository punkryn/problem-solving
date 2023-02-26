# https://www.acmicpc.net/problem/1469
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(depth, idx):
    if depth == n:
        print(*S)
        exit()
    
    for i in range(n):
        if v[i]: continue
        nxt = idx + X[i] + 1
        if S[idx] != -1 or nxt >= n * 2 or S[nxt] != -1:
            continue
        
        v[i] = True
        S[idx] = X[i]
        S[nxt] = X[i]
        nxtIdx = idx + 1
        while nxtIdx < n * 2 and S[nxtIdx] != -1:
            nxtIdx += 1
        go(depth + 1, nxtIdx)
            
        S[nxt] = -1
        S[idx] = -1
        v[i] = False

if __name__ == '__main__':
    n = int(si())
    X = sorted(mis())
    v = [False] * n
    
    ans = -1
    S = [-1] * (n * 2)
    go(0, 0)
    print(-1)