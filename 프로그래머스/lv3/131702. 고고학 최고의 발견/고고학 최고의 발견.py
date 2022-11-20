from itertools import product

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = int(10**9)

def solution(clockHands):
    answer = INF
    
    n = len(clockHands)
    def click(x, y, cnt, state):
        state[x][y] = (state[x][y] + cnt) % 4
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n): continue
            state[nx][ny] = (state[nx][ny] + cnt) % 4

    def isFinish(state):
        for i in range(n):
            for j in range(n):
                if state[i][j]: return False
        return True
    
    for pro in product(range(4), repeat=n):
        cnt = 0
        state = [row[:] for row in clockHands]
        
        for i in range(n):
            p = pro[i]
            if p == 0: continue
            cnt += p
            click(0, i, p, state)
        
        for i in range(1, n):
            for j in range(n):
                if state[i - 1][j]:
                    p = 4 - state[i - 1][j]
                    click(i, j, p, state)
                    cnt += p
        
        if isFinish(state):
            answer = min(answer, cnt)
    
    return answer