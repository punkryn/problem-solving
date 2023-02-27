# https://www.acmicpc.net/problem/2168
import sys
from math import gcd
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    x, y = mis()
    g = gcd(x, y)
    print((x // g + y // g - 1) * gcd(x, y))