# https://www.acmicpc.net/problem/3085
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def swap(x1, y1, x2, y2):
    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]

def check():
    ret = 0
    for i in range(n):
        row = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                row += 1
            else:
                row = 1
            ret = max(ret, row)
    
    for j in range(n):
        col = 1
        for i in range(1, n):
            if board[i][j] == board[i - 1][j]:
                col += 1
            else:
                col = 1
            ret = max(ret, col)
    return ret

if __name__ == '__main__':
    n = int(si())
    board = [list(si().strip()) for _ in range(n)]
    
    ans = 0
    for i in range(n):
        for j in range(n):
            if j + 1 < n:
                swap(i, j, i, j + 1)
                ans = max(ans, check())
                swap(i, j, i, j + 1)
            
            if i + 1 < n:
                swap(i, j, i + 1, j)
                ans = max(ans, check())
                swap(i, j, i + 1, j)
    print(ans)