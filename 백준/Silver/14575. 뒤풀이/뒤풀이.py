# https://www.acmicpc.net/problem/14575
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def deter(s):
    SUM = 0
    for l, r in infos:
        if l > s: return False
        SUM += l
    
    if SUM > t: return False

    if SUM == t: return True
    
    for l, r in infos:
        SUM = SUM - l + min(r, s)
        if SUM >= t:
            return True
    
    return False

if __name__ == '__main__':
    n, t = mis()
    
    infos = [list(mis()) for _ in range(n)]
    
    ans = -1
    l, r = 1, 1_000_000

    while l <= r:
        mid = (l + r) // 2
        
        if deter(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)