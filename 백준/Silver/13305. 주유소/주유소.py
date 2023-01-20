# https://www.acmicpc.net/problem/13305
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    roads = list(mis())
    city = list(mis())

    st = INF
    ans = 0
    for i in range(n - 1):
        if st > city[i]:
            st = city[i]
        
        ans += st * roads[i]
    print(ans)