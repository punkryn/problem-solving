# https://www.acmicpc.net/problem/15664
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(depth, cur, idx):
    if depth == m:
        print(*cur)
        return

    for i in range(idx, n):
        if i == idx:
            cur.append(A[i])
            go(depth + 1, cur, i + 1)
            cur.pop()
        else:
            if A[i] == A[i - 1]:
                continue
            cur.append(A[i])
            go(depth + 1, cur, i + 1)
            cur.pop()


if __name__ == '__main__':
    n, m = mis()
    A = sorted(mis())
    
    go(0, [], 0)