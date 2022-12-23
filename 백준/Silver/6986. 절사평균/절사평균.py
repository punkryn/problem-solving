# https://www.acmicpc.net/problem/6986
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, k = mis()
    scores = sorted([float(si()) for _ in range(n)])
    
    ja = scores[k: n - k]
    print(f'{round(sum(ja) / len(ja) + 1e-8, 2):.2f}')

    print(f'{round((ja[0] * k + ja[-1] * k + sum(ja)) / n + 1e-8, 2):.2f}')