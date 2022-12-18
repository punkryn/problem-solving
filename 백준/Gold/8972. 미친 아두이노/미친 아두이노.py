# https://www.acmicpc.net/problem/8972
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

def solution(ops):
    global ard
    x, y = jongsu
    for idx, op in enumerate(ops, start=1):
        op = int(op)
        nx = x + dx[op]
        ny = y + dy[op]

        if (nx, ny) in ard:
            return False, idx
        
        cand = set()
        des = set()
        for ax, ay in ard:
            minD = INF
            mAx, mAy = ax, ay
            for i in range(1, 10):
                nax = ax + dx[i]
                nay = ay + dy[i]

                if not (0 <= nax < r and 0 <= nay < c): continue
                tmp = abs(nx - nax) + abs(ny - nay)
                if minD > tmp:
                    minD = tmp
                    mAx, mAy = nax, nay
            
            if (mAx, mAy) in cand:
                des.add((mAx, mAy))
            else:
                cand.add((mAx, mAy))
            
            if mAx == nx and mAy == ny:
                return False, idx
        
        for mAx, mAy in des:
            cand.remove((mAx, mAy))
        
        ard = cand
        x, y = nx, ny

    return True, (x, y)
            

if __name__ == '__main__':
    r, c = mis()
    board = [si().strip() for _ in range(r)]

    ard = set()
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                continue

            if board[i][j] == 'I':
                jongsu = (i, j)
            elif board[i][j] == 'R':
                ard.add((i, j))
    
    ops = si().strip()
    res = solution(ops)

    if res[0]:
        v = [['.'] * c for _ in range(r)]
        x, y = res[1]
        v[x][y] = 'I'
        for x, y in ard:
            v[x][y] = 'R'
        
        for row in v:
            print(''.join(row))
    else:
        print(f'kraj {res[1]}')