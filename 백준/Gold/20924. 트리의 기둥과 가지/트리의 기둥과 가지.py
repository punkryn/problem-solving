# https://www.acmicpc.net/problem/20924
import sys
sys.setrecursionlimit(int(1e6))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, prev, length, gal):
    global gi, ga, flag
    if flag and ((prev == -1 and len(tree[x]) >= 2) or len(tree[x]) >= 3):
        flag = False
        gi = length
    
    if x != r and len(tree[x]) == 1:
        ga = max(ga, gal)
        if flag:
            gi = length
        return

    for nxt, d in tree[x]:
        if nxt == prev:
            continue

        if not flag:
            DFS(nxt, x, length, gal + d)
        else:
            DFS(nxt, x, length + d, gal)

if __name__ == '__main__':
    n, r = mis()
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, d = mis()
        tree[a].append((b, d))
        tree[b].append((a, d))
    
    gi = ga = 0
    flag = True
    DFS(r, -1, 0, 0)
    print(gi, ga)