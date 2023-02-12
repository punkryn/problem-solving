# https://www.acmicpc.net/problem/15831
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, B, W = mis()

    s = si().strip()
    ans = 0
    r = 0
    b = w = 0
    for l in range(n):
        while r < n and b <= B:
            if s[r] == 'W':
                w += 1
            else:
                b += 1
            
            r += 1

            if b <= B and w >= W:
                ans = max(ans, r - l)

        if s[l] == 'W':
            w -= 1
        else:
            b -= 1
    print(ans)
        