# https://www.acmicpc.net/problem/14675
import sys
sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, prev):
    if len(tree[x]) == 1:
        leaf.add(x)

        if x != 1:
            return
    
    for nxt in tree[x]:
        if nxt == prev: continue
        DFS(nxt, x)

if __name__ == '__main__':
    n = int(si())
    tree = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = mis()
        tree[a].append(b)
        tree[b].append(a)
    
    leaf = set()
    DFS(1, 0)

    q = int(si())
    for _ in range(q):
        t, k = mis()
        if t == 1:
            print('yes' if k not in leaf else 'no')
        else:
            print('yes')