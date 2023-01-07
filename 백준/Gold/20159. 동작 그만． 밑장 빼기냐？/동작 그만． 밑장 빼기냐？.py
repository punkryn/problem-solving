# https://www.acmicpc.net/problem/20159
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    X = list(mis())
    
    turn = n // 2
    m = [0] * (turn + 1)
    y = [0] * (turn + 1)
    for i in range(1, turn + 1):
        m[i] = m[i - 1] + X[(i - 1) * 2]
    
    for i in range(1, turn + 1):
        y[i] = y[i - 1] + X[(i - 1) * 2 + 1]
    ans = 0
    SUM = 0
    for i in range(1, turn + 1):
        SUM += X[(i - 1) * 2]
        ans = max(ans, SUM, m[i - 1] + y[turn] - y[i - 1], m[i] + y[turn - 1] - y[i - 1])
    print(ans)