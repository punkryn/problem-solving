dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        start = []
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    start.append((i, j))
        
        visited = [[False] * m for _ in range(n)]
        
        def go(x, y, idx):
            if idx == len(word):
                return True

            flag = False
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if visited[nx][ny]: continue
                if board[nx][ny] != word[idx]: continue
                visited[nx][ny] = True
                flag |= go(nx, ny, idx + 1)
                visited[nx][ny] = False
            
            return flag

        for x, y in start:
            visited[x][y] = True
            ans = go(x, y, 1)
            if ans: return ans
            visited[x][y] = False
        return False