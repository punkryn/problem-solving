# https://www.acmicpc.net/problem/26260
import sys
from math import log2
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dnc(l, r, idx):
    if idx > n:
        return
    if l == r:
        nTree[idx] = tree[l]
        return

    mid = (l + r) // 2
    nTree[idx] = tree[mid]
    dnc(l, mid - 1, idx * 2)
    dnc(mid + 1, r, idx * 2 + 1)

def postorder(x):
    if x > n:
        return
    if nTree[x] == INF:
        return
    
    postorder(x * 2)
    postorder(x * 2 + 1)
    print(nTree[x], end=' ')

if __name__ == '__main__':
    n = int(si())
    k = int(log2(n + 1))
    A = list(mis())
    X = int(si())

    tree = [INF] * n
    idx = 0
    for i in range(n):
        if A[i] == -1:
            tree[i] = X
            continue
        tree[i] = A[i]

    tree.sort()
    
    nTree = [0] * (n + 1)
    dnc(0, n, 1)
    
    postorder(1)