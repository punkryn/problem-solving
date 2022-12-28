# https://www.acmicpc.net/problem/2437
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    A = sorted(mis())
    
    ans = 1

    for a in A:
        if ans < a:
            break

        ans += a
    print(ans)