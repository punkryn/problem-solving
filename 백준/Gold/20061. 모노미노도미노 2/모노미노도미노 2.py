# https://www.acmicpc.net/problem/20061
import sys
# sys.setrecursionlimit(int(1e9))
si = sys.stdin.readline
mis = lambda: map(int, si().split())
INF = float('inf')
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

R=0;G=1;B=2

def move(pos):
    pos_ = pos[:]
    while pos_:
        tmp = []
        flag = False
        for x, y in pos_:
            nx = x + 0
            ny = y + 1

            if not ny < 10: 
                flag = True
                break
            if (nx, ny) not in pos_ and board[nx][ny]: 
                flag = True
                break

            tmp.append((nx, ny))
        else:
            for x, y in pos_:
                board[x][y] = 0
            for x, y in tmp:
                board[x][y] = 1
            
            pos_ = tmp

        if flag:
            break

    pos_ = pos[:]
    while pos_:
        tmp = []
        flag = False
        for x, y in pos_:
            nx = x + 1
            ny = y + 0

            if not nx < 10: 
                flag = True
                break
            if (nx, ny) not in pos_ and board[nx][ny]: 
                flag = True
                break

            tmp.append((nx, ny))
        else:
            for x, y in pos_:
                board[x][y] = 0
            for x, y in tmp:
                board[x][y] = 1
            
            pos_ = tmp
        
        if flag:
            break

def fullCheck():
    total = 0
    cand = []
    for i in range(9, 3, -1):
        SUM = 0
        for j in range(4):
            SUM += board[j][i]
        
        if SUM == 4:
            cand.append(i)
    
    total += len(cand)
    for i in cand:
        for j in range(4):
            board[j][i] = 0
    
    if cand:
        for i in range(cand[-1] - 1, 3, -1):
            for j in range(4):
                board[j][i + len(cand)] = board[j][i]
                board[j][i] = 0
    
    cand = []
    for i in range(9, 3, -1):
        SUM = sum(board[i][:4])
        if SUM == 4:
            cand.append(i)
    total += len(cand)
    for i in cand:
        for j in range(4):
            board[i][j] = 0
    
    if cand:
        for i in range(cand[-1] - 1, 3, -1):
            for j in range(4):
                board[i + len(cand)][j] = board[i][j]
                board[i][j] = 0
    
    return total

def borderCheck():
    cand = []
    for i in range(4, 6):
        SUM = 0
        for j in range(4):
            SUM += board[j][i]
        if SUM > 0:
            cand.append(i)
    
    if cand:
        for i in range(9, 9 - len(cand), -1):
            for j in range(4):
                board[j][i] = 0
    
        for i in range(9 - len(cand), 3, -1):
            for j in range(4):
                board[j][i + len(cand)] = board[j][i]
                board[j][i] = 0
    
    cand = []
    for i in range(4, 6):
        SUM = sum(board[i][:4])
        if SUM > 0:
            cand.append(i)
    
    if cand:
        for i in range(9, 9 - len(cand), -1):
            for j in range(4):
                board[i][j] = 0
        
        for i in range(9 - len(cand), 3, -1):
            for j in range(4):
                board[i + len(cand)][j] = board[i][j]
                board[i][j] = 0

def show():
    for bb in board:
        print(bb)

if __name__ == '__main__':
    n = int(si())
    board = [[0] * 10 for _ in range(10)]
    
    ans = 0
    for _ in range(n):
        t, x, y = mis()
        if t == 1:
            move([(x, y)])
        elif t == 2:
            move([(x, y), (x, y + 1)])
        else:
            move([(x, y), (x + 1, y)])
        ans += fullCheck()
        borderCheck()

    print(ans)
    print(sum(sum(b) for b in board))