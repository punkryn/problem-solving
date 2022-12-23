# https://www.acmicpc.net/problem/15999
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

MOD = 10 ** 9 + 7

def dfs(x, y, w):
    q = [(x, y)]
    v[x][y] = True

    cnt = 0
    while q:
        x, y = q.pop()

        flag = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if grid[nx][ny] != w: 
                flag = False
                continue
            if v[nx][ny]: continue
            
            v[nx][ny] = True
            q.append((nx, ny))

        if flag:
            cnt += 1
    return cnt

if __name__ == '__main__':
    n, m = mis()
    grid = [si().strip() for _ in range(n)]

    v = [[False] * m for _ in range(n)]
    ans = 1
    for i in range(n):
        for j in range(m):
            if v[i][j]: continue

            cnt = dfs(i, j, grid[i][j])
            if cnt == 0:
                continue
            tmp = 1
            while cnt:
                tmp = (tmp << min(cnt, 30)) % MOD
                cnt -= min(cnt, 30)

            ans = (ans * tmp) % MOD
    print(ans)