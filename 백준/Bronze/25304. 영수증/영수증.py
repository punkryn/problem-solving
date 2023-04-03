import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    X = int(si())
    N = int(si())
    ans = 0
    for _ in range(N):
        a, b = mis()
        ans += a * b
    print('Yes' if ans == X else 'No')