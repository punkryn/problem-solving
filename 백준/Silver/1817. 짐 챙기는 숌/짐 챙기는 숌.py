# https://www.acmicpc.net/problem/1817
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = mis()
    if n == 0:
        print(0)
        exit()
    w = list(mis())

    ans = 1
    cur = 0
    for i in range(n):
        nxt = cur + w[i]
        if nxt > m:
            cur = w[i]
            ans += 1
            continue

        cur = nxt
    print(ans)