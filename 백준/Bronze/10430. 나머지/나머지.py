import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    a,b,c=mis()
    print((a+b)%c)
    print((a+b)%c)
    print((a*b)%c)
    print((a*b)%c)