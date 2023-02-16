# https://www.acmicpc.net/problem/3673
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    for _ in range(int(si())):
        d, n = mis()
        A = list(mis())
        
        r = [0] * (d + 1)

        ans = 0
        SUM = 0
        for i in range(n):
            SUM = (SUM + A[i]) % d
            
            ans += r[SUM] + (1 if SUM == 0 else 0)

            r[SUM] += 1
        print(ans)