# https://www.acmicpc.net/problem/17123
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    for _ in range(int(si())):
        n, m = mis()
        A = [list(mis()) for _ in range(n)]
        
        ps = [[0] * (n + 1) for _ in range(n + 1)]
        for _ in range(m):
            r1, c1, r2, c2, v = mis()
            r1 -= 1; c1 -= 1; r2 -= 1; c2 -= 1
            
            ps[r1][c1] += v
            ps[r1][c2 + 1] -= v
            ps[r2 + 1][c1] -= v
            ps[r2 + 1][c2 + 1] += v
        
        for i in range(n):
            for j in range(1, n + 1):
                ps[i][j] += ps[i][j - 1]
        
        for j in range(n):
            for i in range(1, n + 1):
                ps[i][j] += ps[i - 1][j]
        
        for i in range(n):
            for j in range(n):
                A[i][j] += ps[i][j]
        
        print(*[sum(row) for row in A])
        
        for j in range(n):
            col = 0
            for i in range(n):
                col += A[i][j]
            print(col, end=' ')
        print()