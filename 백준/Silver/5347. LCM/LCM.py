# https://www.acmicpc.net/problem/5347
import sys
from math import gcd
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    for _ in range(n):
        a, b = mis()
        g = gcd(a, b)
        print((a // g) * (b // g) * g)