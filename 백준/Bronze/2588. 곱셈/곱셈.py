import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    a = int(si())
    b = int(si())
    ans = a * b
    while b:
        c = b % 10
        print(a * c)
        b //= 10
    print(ans)