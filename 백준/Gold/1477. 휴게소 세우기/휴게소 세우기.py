# https://www.acmicpc.net/problem/1477
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def deter(mid):
    cnt = 0
    cur = 0
    for i in range(n + 1):
        while pos[i] - cur > mid:
            if cnt == m:
                return False
            
            cnt += 1
            cur += mid
        cur = pos[i]
    return cnt <= m

if __name__ == '__main__':
    n, m, length = mis()
    pos = sorted(mis()) + [length]

    l, r = 0, 1_000
    ans = 0
    while l <= r:
        mid = (l + r) // 2

        if deter(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)