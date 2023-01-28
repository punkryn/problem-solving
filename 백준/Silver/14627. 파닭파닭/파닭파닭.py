# https://www.acmicpc.net/problem/14627
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def deter(mid):
    cnt = sum([row // mid for row in L])
    return cnt >= c

if __name__ == '__main__':
    s, c = mis()

    L = [int(si()) for _ in range(s)]
    ml = min(L)

    l, r = 1, int(1e9)
    ans = 0
    while l <= r:
        mid = (l + r) // 2

        if deter(mid):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    
    cnt = 0
    answer = 0
    for l in L:
        if cnt + l // ans > c:
            answer += (c - cnt) * ans
            break
        cnt += l // ans
        answer += l % ans
    print(answer)