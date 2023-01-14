# https://www.acmicpc.net/problem/11478
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    S = si().strip()

    n = len(S)
    v = set()
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            v.add(S[j: j + i])
    print(len(v))