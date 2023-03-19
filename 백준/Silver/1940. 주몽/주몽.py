# https://www.acmicpc.net/problem/1940
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    m = int(si())
    a = set(mis())
    b = set([a_ for a_ in a])
    ans = 0
    for x in a:
        y = m - x
        if x in b:
            b.remove(x)
        if y in b:
            ans += 1
            b.remove(y)
    print(ans)