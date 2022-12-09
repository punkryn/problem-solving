# https://www.acmicpc.net/problem/18809
import sys
from collections import deque
from itertools import combinations
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

RED = 1
GREEN = 2

if __name__ == '__main__':
    n, m, g, r = mis()
    
    ground = [list(mis()) for _ in range(n)]
    cand = []
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 2:
                cand.append((i, j))
    
    ans = 0
    for comb in combinations(range(len(cand)), g):
        r_cands = set(range(len(cand)))
        for c in comb:
            r_cands.remove(c)
        
        for r_cand in combinations(r_cands, r):
            q = deque()
            v = [[-1] * m for _ in range(n)]
            color = [[0] * m for _ in range(n)]
            for c in comb:
                q.append((*cand[c], GREEN))
                v[cand[c][0]][cand[c][1]] = 0
                color[cand[c][0]][cand[c][1]] = RED
            
            for red in r_cand:
                q.append((*cand[red], RED))
                v[cand[red][0]][cand[red][1]] = 0
                color[cand[red][0]][cand[red][1]] = GREEN
            
            cnt = 0
            while q:
                nxtQ = deque()
                while q:
                    x, y, TYPE = q.popleft()
                    if v[x][y] == -2:
                        continue

                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]

                        if not (0 <= nx < n and 0 <= ny < m): continue
                        if ground[nx][ny] == 0: continue
                        if v[nx][ny] == -2: continue
                        if v[nx][ny] != -1:
                            if TYPE != color[nx][ny] and v[nx][ny] == v[x][y] + 1:
                                cnt += 1
                                v[nx][ny] = -2
                            continue

                        v[nx][ny] = v[x][y] + 1
                        color[nx][ny] = TYPE
                        nxtQ.append((nx, ny, TYPE))
                
                q = nxtQ
            ans = max(ans, cnt)

    print(ans)