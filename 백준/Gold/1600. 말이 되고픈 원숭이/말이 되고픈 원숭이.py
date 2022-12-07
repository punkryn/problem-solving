# https://www.acmicpc.net/problem/1600
import sys
from collections import deque
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ddx = [-2, -1, 1, 2, 2, 1, -1, -2]
ddy = [1, 2, 2, 1, -1, -2, -2, -1]

def OOB(x, y):
    if not (0 <= x < h and 0 <= y < w):
        return True
    return False

if __name__ == '__main__':
    k = int(si())
    w, h = mis()
    grid = [list(mis()) for _ in range(h)]

    q = deque([(0, 0, 0)])
    v = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]
    v[0][0][0] = 0

    while q:
        x, y, cnt = q.popleft()

        if x == h - 1 and y == w - 1:
            break

        for i in range(8):
            if cnt >= k: break
            nnx = x + ddx[i]
            nny = y + ddy[i]
            
            if OOB(nnx, nny): continue
            if grid[nnx][nny]: continue
            if v[nnx][nny][cnt + 1] != -1: continue
            
            v[nnx][nny][cnt + 1] = v[x][y][cnt] + 1
            q.append((nnx, nny, cnt + 1))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if OOB(nx, ny): continue
            if grid[nx][ny]: continue
            if v[nx][ny][cnt] != -1: continue

            v[nx][ny][cnt] = v[x][y][cnt] + 1
            q.append((nx, ny, cnt))

    ans = INF
    for i in range(k + 1):
        if v[h - 1][w - 1][i] == -1: continue
        ans = min(ans, v[h - 1][w - 1][i])
    
    print(ans if ans != INF else -1)