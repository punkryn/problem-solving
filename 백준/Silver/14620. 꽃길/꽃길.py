# https://www.acmicpc.net/problem/14620
import sys
from itertools import combinations
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    grid = [list(mis()) for _ in range(n)]

    ans = INF
    for comb in combinations(range(n * n), 3):
        a, b, c = comb
        na_, nb_, nc_ = (a // n, a % n), (b // n, b % n), (c // n, c % n)
        v = set([na_, nb_, nc_])
        flag = False
        for x in [a, b, c]:
            r, c = x // n, x % n
            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]

                if not (0 <= nr < n and 0 <= nc < n):
                    flag = True
                    break

                if (nr, nc) in v:
                    flag = True
                    break

                v.add((nr, nc))
            
            if flag:
                break
        
        if flag:
            continue

        ans = min(ans, sum([grid[x][y] for x, y in v]))
    print(ans)