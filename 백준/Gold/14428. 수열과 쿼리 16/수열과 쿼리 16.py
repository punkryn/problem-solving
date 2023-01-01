# https://www.acmicpc.net/problem/14428
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def comp(x, y):
    if x == INF: return y
    if y == INF: return x

    if A[x] == A[y]:
        return x if x < y else y
    else:
        return x if A[x] <= A[y] else y

def init(l, r, idx):
    if l == r:
        seg[idx] = l
        return seg[idx]
    
    mid = (l + r) // 2
    ret = comp(init(l, mid, idx * 2), init(mid + 1, r, idx * 2 + 1))
    seg[idx] = ret
    return seg[idx]

def query(l, r, idx, i, j):
    if r < i or j < l:
        return INF
    
    if i <= l and r <= j:
        return seg[idx]
    
    mid = (l + r) // 2
    return comp(query(l, mid, idx * 2, i, j), query(mid + 1, r, idx * 2 + 1, i, j))

def update(l, r, idx, i, v):
    if i < l or r < i:
        return seg[idx]
    
    if l == r:
        return seg[idx]

    mid = (l + r) // 2
    ret = comp(update(l, mid, idx * 2, i, v), update(mid + 1, r, idx * 2 + 1, i, v))
    seg[idx] = ret
    return seg[idx]

if __name__ == '__main__':
    n = int(si())
    A = list(mis())

    seg = [INF] * (n * 4)
    init(0, n - 1, 1)

    for _ in range(int(si())):
        op, *args = mis()
        if op == 1:
            i, v = args
            A[i - 1] = v
            update(0, n - 1, 1, i - 1, v)
        else:
            i, j = args
            print(query(0, n - 1, 1, i - 1, j - 1) + 1)