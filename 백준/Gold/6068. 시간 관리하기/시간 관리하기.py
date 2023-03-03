# https://www.acmicpc.net/problem/6068
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    TS = sorted([list(mis()) for _ in range(n)], key=lambda x: (x[1], x[0]))
    ans = INF
    for i in range(n - 1, -1, -1):
        ans = min(ans, TS[i][1])
        ans -= TS[i][0]
    
    print(-1 if ans < 0 else ans)