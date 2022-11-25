# https://www.acmicpc.net/problem/6209
import sys
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def deter(mid):
    cnt = 0
    cur = 0
    for i in range(n):
        diff = stone[i] - cur
        if diff < mid:
            cnt += 1
        else:
            cur = stone[i]
        if cnt > m:
            return False
    return True

if __name__ == '__main__':
    d, n, m = mis()
    stone = sorted([int(si()) for _ in range(n)])

    l, r = 1, d
    ans = 0
    while l <= r:
        mid = (l + r) // 2

        if deter(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    print(ans)