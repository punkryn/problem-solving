# https://www.acmicpc.net/problem/16401
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def deter(mid):
    cnt = 0
    for i in range(n):
        cnt += L[i] // mid
    return cnt >= m

if __name__ == '__main__':
    m, n = mis()
    L = list(mis())
    
    ans = 0
    l, r = 1, 1_000_000_000
    while l <= r:
        mid = (l + r) // 2
        
        if deter(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    print(ans)