# https://www.acmicpc.net/problem/11559
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, puyo, v):
    group = [(x, y)]
    q = [(x, y)]
    v[x][y] = True
    while q:
        x, y = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < 12 and 0 <= ny < 6):
                continue

            if v[nx][ny]: continue
            if field[nx][ny] != puyo: continue

            group.append((nx, ny))
            v[nx][ny] = True
            q.append((nx, ny))

    return group

def getCandidate():
    cand = []
    
    v = [[False] * 6 for _ in range(12)]
    for i in range(11, -1, -1):
        for j in range(6):
            if field[i][j] == '.': continue
            if v[i][j]: continue
            group = DFS(i, j, field[i][j], v)
            if len(group) < 4: continue

            cand.append(group)
    
    return cand

def removePuyo(cand):
    for group in cand:
        for x, y in group:
            field[x][y] = '.'

def fallPuyo():
    for i in range(10, -1, -1):
        for j in range(6):
            if field[i][j] == '.': continue
            cur = i
            while cur < 11 and field[cur + 1][j] == '.':
                tmp = field[cur][j]
                field[cur][j] = '.'
                field[cur + 1][j] = tmp
                cur += 1
                    

if __name__ == '__main__':
    field = [list(si().strip()) for _ in range(12)]
    
    ans = 0
    while True:
        cand = getCandidate()

        if len(cand) == 0:
            break

        ans += 1
        removePuyo(cand)
        fallPuyo()
    print(ans)