# https://www.acmicpc.net/problem/2931
import sys
from collections import deque
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def flow(b):
    q = deque([(mos[0], mos[1], 0)])

    check = dict()
    
    while q:
        x, y, d = q.popleft()
        if not (0 <= x < r and 0 <= y < c):
            continue
        
        if block[x][y] == '.':
            return False, (x, y)
        
        if block[x][y] == 'M':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < r and 0 <= ny < c):
                    continue
                
                if block[nx][ny] == '.' or block[nx][ny] == 'Z':
                    continue

                q.append((nx, ny, i))
        elif block[x][y] == 'Z':
            for key in check:
                if len(check[key]) != 2:
                    return False, False
            return True, False
        elif block[x][y] == '-':
            if d == 1 or d == 3:
                nx = x + dx[d]
                ny = y + dy[d]

                q.append((nx, ny, d))
        elif block[x][y] == '|':
            if d == 0 or d == 2:
                nx = x + dx[d]
                ny = y + dy[d]

                q.append((nx, ny, d))
        elif block[x][y] == '+':
            nx = x + dx[d]
            ny = y + dy[d]

            if (x, y) not in check:
                check[(x, y)] = set()
            
            check[(x, y)].add(d)

            q.append((nx, ny, d))
        elif block[x][y] == '1':
            if d == 0:
                nx = x + dx[1]
                ny = y + dy[1]

                q.append((nx, ny, 1))
            elif d == 3:
                nx = x + dx[2]
                ny = y + dy[2]

                q.append((nx, ny, 2))
        elif block[x][y] == '2':
            if d == 2:
                nx = x + dx[1]
                ny = y + dy[1]

                q.append((nx, ny, 1))
            elif d == 3:
                nx = x + dx[0]
                ny = y + dy[0]

                q.append((nx, ny, 0))
        elif block[x][y] == '3':
            if d == 1:
                nx = x + dx[0]
                ny = y + dy[0]

                q.append((nx, ny, 0))
            elif d == 2:
                nx = x + dx[3]
                ny = y + dy[3]

                q.append((nx, ny, 3))
            else:
                return False, False
        elif block[x][y] == '4':
            if d == 1:
                nx = x + dx[2]
                ny = y + dy[2]

                q.append((nx, ny, 2))
            elif d == 0:
                nx = x + dx[3]
                ny = y + dy[3]

                q.append((nx, ny, 3))
    return False, False
        
if __name__ == '__main__':
    r, c = mis()
    block = [list(si().strip()) for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if block[i][j] == '.':
                continue

            if block[i][j] == 'M':
                mos = (i, j)
            elif block[i][j] == 'Z':
                zag = (i, j)
    
    _, pos = flow('')
    if not pos:
        if mos[0] == zag[0]:
            x, y = mos[0], (mos[1] + zag[1]) // 2
        elif mos[1] == zag[1]:
            x, y = (mos[0] + zag[0]) // 2, mos[1]
        
    else:
        x, y = pos

    for b in ['|', '-', '+', '1', '2', '3' ,'4']:
        block[x][y] = b
        ret = flow(b)

        if ret[0]:
            print(x + 1, y + 1, b)
            exit()