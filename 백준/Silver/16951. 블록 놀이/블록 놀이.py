# https://www.acmicpc.net/problem/16951
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, k = mis()
    A = list(mis())

    ans = INF
    for i in range(n):
        tmp = 0
        for j in range(n):
            cur = k * ( j - i) + A[i]
            if cur < 1:
                tmp = INF
                break

            if cur != A[j]:
                tmp += 1
        
        ans = min(ans, tmp)
    print(ans)