# https://www.acmicpc.net/problem/16206
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n, m = mis()
    A = sorted(list(mis()), key=lambda x: (x % 10 != 0, x))
    
    ans = 0
    cnt = 0
    for i in range(n):
        if A[i] % 10 == 0:
            nxt = A[i] // 10 - 1
            nxtCnt = cnt + nxt
            
            if nxtCnt > m:
                ans += m - cnt
                break
            ans += A[i] // 10
            cnt = nxtCnt
            continue

        nxt = A[i] // 10
        nxtCnt = cnt + nxt

        if nxtCnt > m:
            ans += m - cnt
            break

        ans += nxt
        cnt = nxtCnt
    print(ans)