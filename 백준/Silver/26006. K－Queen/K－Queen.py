# https://www.acmicpc.net/problem/26006
import sys
sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

if __name__ == '__main__':
    n, k = mis()
    r, c = mis()

    cand = []
    for i in range(8):
        nr = r + dx[i]
        nc = c + dy[i]
        if not (1 <= nr <= n and 1 <= nc <= n): continue
        cand.append((nr, nc))
    
    cnt = [0] * len(cand)
    ans = 0
    for _ in range(k):
        a, b = mis()
        for i in range(len(cand)):
            x, y = cand[i]
            if abs(x - a) == abs(y - b):
                cnt[i] = 1
            elif a == x:
                cnt[i] = 1
            elif b == y:
                cnt[i] = 1
                
        if abs(a - r) == abs(b - c):
            ans = 1
        elif r == a:
            ans = 1
        elif c == b:
            ans = 1
    
    if ans == 1 and sum(cnt) == len(cand):
        print('CHECKMATE')
    elif ans == 1 and sum(cnt) < len(cand):
        print('CHECK')
    elif sum(cnt) == len(cand):
        print('STALEMATE')
    else:
        print('NONE')