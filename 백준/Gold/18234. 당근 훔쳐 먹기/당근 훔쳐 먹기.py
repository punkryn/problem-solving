# https://www.acmicpc.net/problem/18234
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, t = mis()
    wp = sorted([list(mis()) for _ in range(n)], key=lambda x: x[1])

    d = t - n
    ans = 0
    for i in range(n):
        w, p = wp[i]

        ans += w + p * d

        d += 1
    print(ans)