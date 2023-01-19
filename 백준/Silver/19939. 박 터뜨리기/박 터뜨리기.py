# https://www.acmicpc.net/problem/19939
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, k = mis()
    SUM = ((1 + k) * (k // 2) + (1 + k) // 2) if k % 2 == 1 else ((1 + k) * (k // 2))
    if SUM > n:
        print(-1)
        exit()
    
    print(k - 1 + (1 if (n - SUM) % k else 0))