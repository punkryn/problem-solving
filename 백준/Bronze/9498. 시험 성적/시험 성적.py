import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    if 90 <= n <= 100:
        print('A')
    elif 80 <= n:
        print('B')
    elif 70 <= n:
        print('C')
    elif 60 <= n:
        print('D')
    else:
        print('F')