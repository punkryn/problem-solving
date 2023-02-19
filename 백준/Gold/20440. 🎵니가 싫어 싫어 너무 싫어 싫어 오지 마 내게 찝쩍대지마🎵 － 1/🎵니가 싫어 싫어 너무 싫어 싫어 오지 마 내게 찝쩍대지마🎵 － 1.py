# https://www.acmicpc.net/problem/20440
import sys
from collections import defaultdict
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

if __name__ == '__main__':
    n = int(si())
    T = defaultdict(int)
    for _ in range(n):
        e, x = mis()
        T[e] += 1
        T[x] -= 1
    
    ans = 0
    cnt = 0
    tem = txm = 0
    flag = False
    for t in sorted(T.keys()):
        cnt += T[t]
        if cnt > ans:
            ans = cnt
            tem = t
            flag = True
        elif flag and cnt < ans and cnt == ans + T[t]:
            txm = t
            flag = False
    print(ans)
    print(tem, txm)