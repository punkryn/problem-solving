# https://www.acmicpc.net/problem/17090
import sys
sys.setrecursionlimit(250_001)
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')

d = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
}

CYCLE=3
ESCAPE=2
VISITED=1
NOT_VISITED=0

def DFS(x, y):
    dx, dy = d[maze[x][y]]
    nx, ny = x + dx, y + dy

    ret = -1
    if not (0 <= nx < n and 0 <= ny < m):
        ret = ESCAPE
    else:
        if v[nx][ny] == NOT_VISITED:
            v[nx][ny] = VISITED
            ret = DFS(nx, ny)
            v[nx][ny] = ret
        elif v[nx][ny] == VISITED:
            ret = CYCLE
        elif v[nx][ny] == ESCAPE:
            ret = ESCAPE
        else:
            ret = CYCLE
    return ret
            

if __name__ == '__main__':
    n, m = mis()
    maze = [si().strip() for _ in range(n)]
    v = [[NOT_VISITED] * m for _ in range(n)]

    ans = 0
    for i in range(n):
        for j in range(m):
            if v[i][j] != NOT_VISITED:
                continue
            
            v[i][j] = VISITED
            v[i][j] = DFS(i, j)
    
    print(sum([1 for i in range(n) for j in range(m) if v[i][j] == ESCAPE]))