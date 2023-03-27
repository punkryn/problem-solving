import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    A, B = mis()
    C = int(si())
    
    m = A * 60 + B + C
    H = (m // 60) % 24
    M = m % 60
    print(H, M)