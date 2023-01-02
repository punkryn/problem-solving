# https://www.acmicpc.net/problem/2268
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def SUM(l, r, idx, i, j):
    if r < i or j < l:
        return 0
    
    if i <= l and r <= j:
        return seg[idx]
    
    mid = (l + r) // 2
    
    return SUM(l, mid, idx * 2, i, j) + SUM(mid + 1, r, idx * 2 + 1, i, j)

def MODIFY(l, r, idx, i, diff):
    if r < i or i < l:
        return
    
    seg[idx] += diff

    if l == r:
        return

    mid = (l + r) // 2
    MODIFY(l, mid, idx * 2, i, diff)
    MODIFY(mid + 1, r, idx * 2 + 1, i, diff)
    

if __name__ == '__main__':
    n, m = mis()

    A = [0] * (n + 1)
    seg = [0] * (n * 4)
    
    for _ in range(m):
        op, *args = mis()
        if op == 0:
            i, j = args
            if i > j:
                i, j = j, i
            
            print(SUM(1, n, 1, i, j))
        else:
            i, k = args
            diff = k - A[i]
            A[i] = k
            MODIFY(1, n, 1, i, diff)