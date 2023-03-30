import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    x = int(si())
    y = int(si())

    if x > 0 and y > 0:
        print(1)
    elif y > 0:
        print(2)
    elif x > 0:
        print(4)
    else:
        print(3)