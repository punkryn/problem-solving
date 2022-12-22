# https://www.acmicpc.net/problem/9024
import sys
from collections import defaultdict
from bisect import bisect
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    for _ in range(int(si())):
        n, k = mis()
        A = sorted(mis())

        l, r = 0, n - 1
        ans = defaultdict(int)
        mv = INF
        while l < r:
            SUM = A[l] + A[r]
            if mv > abs(SUM - k):
                mv = abs(SUM - k)
            ans[SUM] += 1

            if SUM < k:
                l += 1
            else:
                r -= 1

        if mv == 0:
            print(ans[k])
        else:
            print(ans[k + mv] + ans[k - mv])