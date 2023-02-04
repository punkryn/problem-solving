# https://www.acmicpc.net/problem/15665
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def go(depth, cur):
    if depth == m:
        print(*cur)
        return
    
    for i in range(n):
        if i != 0:
            if A[i - 1] == A[i]:
                continue
            
            cur.append(A[i])
            go(depth + 1, cur)
            cur.pop()
            continue
        
        cur.append(A[i])
        go(depth + 1, cur)
        cur.pop()

if __name__ == '__main__':
    n, m = mis()
    A = sorted(mis())

    go(0, [])