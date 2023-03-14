# https://www.acmicpc.net/problem/16437
import sys
sys.setrecursionlimit(int(1e5))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, prev):
    ret = SW[x]
    for nxt in tree[x]:
        if nxt == prev: continue
        ret += DFS(nxt, x)
    return ret if ret > 0 else 0
        

if __name__ == '__main__':
    n = int(si())
    tree = [[] for _ in range(n + 1)]

    SW = [0] * (n + 1)

    for i in range(2, n + 1):
        t, a, p = si().split()
        a = int(a); p = int(p)
        tree[i].append(p)
        tree[p].append(i)
        
        if t == 'S':
            SW[i] = a
        else:
            SW[i] = -a
    print(DFS(1, 0))