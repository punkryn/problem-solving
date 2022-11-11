# https://www.acmicpc.net/problem/25977
import sys
from itertools import combinations
si = sys.stdin.readline
mis = lambda: map(int, si().split())

def go(x):
    global cnt
    for nxt in graph[x]:
        if nxt not in _set: continue
        cnt += 1
        go(nxt)

if __name__ == '__main__':
    n, k = mis()
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = mis()
        graph[a].append(b)
    node = list(mis())

    apple_node = []
    remain = []
    for i in range(n):
        if node[i] == 1:
            apple_node.append(i)
        else:
            remain.append(i)
    
    ans = 0
    for i in range(k + 1):
        for apple in combinations(apple_node, i):
            apple = set(apple)
            for j in range(1, len(remain) + 1):
                for pear in combinations(remain, j):
                    _set = apple | set(pear)
                    if 0 not in _set: continue

                    cnt = 1
                    go(0)

                    if cnt != i + j: continue
                    
                    ans = max(ans, sum([1 for p in pear if node[p] == 2]))
    print(ans)