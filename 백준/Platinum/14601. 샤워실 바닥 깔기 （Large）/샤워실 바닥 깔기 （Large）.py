# https://www.acmicpc.net/problem/14601
# 트로미노 퍼즐
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, -1, 0]
dy = [-1, -1, 0, 0]

def check(l, r, u, d):
    for i in range(u, d):
        for j in range(l, r):
            if ans[i][j] != -2:
                lr = (l + r) // 2
                ud = (u + d) // 2
                if l <= j < lr and u <= i < ud:
                    return 0  
                elif lr <= j < r and u <= i < ud:
                    return 1
                elif l <= j < lr and ud <= i < d:
                    return 2
                else:
                    return 3

def go(l, r, u, d):
    global cnt
    if r - l == 1:
        return
    
    cnt += 1
    square = check(l, r, u, d)
    lr = (l + r) // 2
    ud = (u + d) // 2
    tmp = set([0, 1, 2, 3])
    tmp.remove(square)
    for i in tmp:
        nlr = lr + dx[i]
        nud = ud + dy[i]

        ans[nud][nlr] = cnt
    
    go(l, lr, u, ud)
    go(lr, r, u, ud)
    go(l, lr, ud, d)
    go(lr, r, ud, d)

if __name__ == '__main__':
    k = int(si())
    x, y = mis()
    x -= 1; y -= 1

    ans = [[-2] * (1 << k) for _ in range(1 << k)]
    ans[y][x] = -1

    cnt = 0

    go(0, 1 << k, 0, 1 << k)
    
    for a in ans[::-1]:
        print(*a)