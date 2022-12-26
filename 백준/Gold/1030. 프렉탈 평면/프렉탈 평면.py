# https://www.acmicpc.net/problem/1030
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dnc(l, r, u, d, point):
    global revise
    if point == 0:
        return

    if r < c1 or c2 < l or d < r1 or r2 < u:
        return
    
    tmp = (n - k) // 2
    if point == 1:
        for i in range(u, d + 1):
            for j in range(l, r + 1):
                if not (c1 <= j <= c2 and r1 <= i <= r2):
                    continue
                
                if l + tmp <= j < l + tmp + k and u + tmp <= i < u + tmp + k:
                    continue
                
                ans[i - revise[0]][j - revise[1]] = '0'

    u_ = u
    for i in range(n):
        l_ = l
        for j in range(n):
            if tmp <= j < tmp + k and tmp <= i < tmp + k:
                l_ += point
                continue
            dnc(l_, l_ + point - 1, u_, u_ + point - 1, point // n)
            l_ += point
        u_ += point

if __name__ == '__main__':
    s, n, k, r1, r2, c1, c2 = mis()

    if s == 0:
        print('0')
        exit()

    revise = (r1, c1)

    ans = [['1'] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
    dnc(0, (n ** s) - 1, 0, (n ** s) - 1, n ** (s - 1))
    for a in ans:
        print(''.join(a))