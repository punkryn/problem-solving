# https://www.acmicpc.net/problem/1135
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(x):
    if len(tree[x]) == 0:
        return 0
    
    sub = []
    for nxt in tree[x]:
        sub.append(go(nxt))

    ret = 0
    for i, node in enumerate(sorted(sub, reverse=True), start=1):
        ret = max(ret, node + i)
    return ret

if __name__ == '__main__':
    n = int(si())
    tree = [[] for _ in range(n)]
    parent = list(mis())

    for i in range(1, n):
        tree[parent[i]].append(i)
    
    print(go(0))