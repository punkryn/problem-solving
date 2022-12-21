# https://www.acmicpc.net/problem/11687
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def deter(mid):
    cnt = 0
    while mid >= 5:
        cnt += mid // 5
        mid //= 5
    return cnt

if __name__ == '__main__':
    m = int(si())

    l, r = 1, 10 ** 9
    ans = -1
    while l <= r:
        mid = (l + r) // 2

        if deter(mid) >= m:
            r = mid - 1
            ans = mid
        else:
            l = mid + 1
    print(ans if deter(ans) == m else -1)