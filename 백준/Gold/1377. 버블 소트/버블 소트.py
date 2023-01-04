# https://www.acmicpc.net/problem/1377
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    A = sorted(enumerate([int(si()) for _ in range(n)]), key=lambda x: x[1])
    ans = 0
    for i, (x, y) in enumerate(A):
        ans = max(ans, x - i + 1)
    print(ans)