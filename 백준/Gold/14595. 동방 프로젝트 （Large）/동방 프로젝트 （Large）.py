# https://www.acmicpc.net/problem/14595
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    m = int(si())

    e = [0] * (n + 1)
    for _ in range(m):
        a, b = mis()
        e[a] += 1
        e[b] -= 1
    
    for i in range(1, n + 1):
        e[i] += e[i - 1]
    
    ans = 0
    for i in range(1, n + 1):
        if e[i] == 0:
            ans += 1

    print(ans)