# https://www.acmicpc.net/problem/25691
import sys
from itertools import combinations
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def go(x, prev):
    global cnt, v
    for nxt in graph[x]:
        if nxt == prev: continue
        if nxt not in cand: continue

        v += 1
        cnt += tree[nxt]
        go(nxt, x)


if __name__ == '__main__':
    n, k = mis()
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        p, c = mis()
        graph[p].append(c)
    tree = list(mis())

    ans = 0
    for comb in combinations(range(1, n), k - 1):
        cnt = tree[0]
        cand = set(comb) | set([0])
        v = 1
        
        go(0, -1)
        if v == k:
            ans = max(ans, cnt)
    print(ans)