# https://www.acmicpc.net/problem/10868
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def init(l, r, idx):
    if l == r:
        seg[idx] = A[l]
        return A[l]
    
    mid = (l + r) // 2
    ret = min(init(l, mid, idx * 2), init(mid + 1, r, idx * 2 + 1))

    seg[idx] = ret
    return seg[idx]

def query(l, r, idx, a, b):
    if r < a or b < l:
        return INF
    
    if a <= l and r <= b:
        return seg[idx]
    
    mid = (l + r) // 2
    return min(query(l, mid, idx * 2, a, b), query(mid + 1, r, idx * 2 + 1, a, b))

if __name__ == '__main__':
    n, m = mis()

    A = [int(si()) for _ in range(n)]

    seg = [INF] * (n * 4)

    init(0, n - 1, 1)
    
    for _ in range(m):
        a, b = mis()
        print(query(0, n - 1, 1, a - 1, b - 1))