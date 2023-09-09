from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solution(board):
    def move(x, y, d):
        while True:
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < n and 0 <= ny < m) or board[nx][ny] == 'D':
                break
            x += dx[d]
            y += dy[d]
        return x, y
    
    
    answer = -1
    n = len(board)
    m = len(board[0])
    
    q = deque()
    visited = [[-1] * m for _ in range(n)]
    goal = (0, 0)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i, j))
                visited[i][j] = 0
            if board[i][j] == 'G':
                goal = (i, j)
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = move(x, y, i)
            
            if visited[nx][ny] != -1:
                continue
            
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
    
    for v in visited:
        print(v)
    
    return visited[goal[0]][goal[1]]