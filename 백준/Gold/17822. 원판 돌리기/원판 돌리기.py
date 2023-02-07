# https://www.acmicpc.net/problem/17822
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def rotate(x, d, k):
    while k:
        if d == 0:
            disk[x].appendleft(disk[x].pop())
        else:
            disk[x].append(disk[x].popleft())
        k -= 1

def check():
    cand = set()
    for i in range(n):
        for j in range(m):
            if disk[i][j] == 0:
                continue
            if disk[i][j] == disk[i][(j + 1) % m]:
                cand.add((i, j))
            if disk[i][j] == disk[i][(j - 1) % m]:
                cand.add((i, j))

            if i > 0:
                if disk[i][j] == disk[i - 1][j]:
                    cand.add((i, j))
            if i < n - 1:
                if disk[i][j] == disk[i + 1][j]:
                    cand.add((i, j))
    
    for i, j in cand:
        disk[i][j] = 0
    
    if not cand:
        cnt = 0
        SUM = 0
        for i in range(n):
            for j in range(m):
                if disk[i][j] != 0:
                    cnt += 1
                    SUM += disk[i][j]
        
        if cnt:
            avg = SUM / cnt
            for i in range(n):
                for j in range(m):
                    if disk[i][j] == 0:
                        continue

                    if disk[i][j] > avg:
                        disk[i][j] -= 1
                    elif disk[i][j] < avg:
                        disk[i][j] += 1

if __name__ == '__main__':
    n, m, t = mis()
    disk = [deque(list(mis())) for _ in range(n)]

    for _ in range(t):
        x, d, k = mis()
        cur = x
        while cur <= n:
            idx = cur - 1

            rotate(idx, d, k)

            cur += x
        check()
    
    print(sum(sum(row) for row in disk))