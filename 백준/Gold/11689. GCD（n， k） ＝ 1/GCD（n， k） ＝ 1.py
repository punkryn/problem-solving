# https://www.acmicpc.net/problem/11689
import sys
from math import sqrt
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())

    e = n
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            e = e // i * (i - 1)
        while n % i == 0:
            n = n // i
    
    print(e if n == 1 else e // n * (n - 1))