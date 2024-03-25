class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        n = len(grid)
        m = len(grid[0])

        answer = 0
        def go(x, y, visited, total):
            nonlocal answer

            answer = max(answer, total)

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                
                if visited[nx][ny]: continue
                if grid[nx][ny] == 0: continue
                
                visited[nx][ny] = 1
                go(nx, ny, visited, total + grid[nx][ny])
                visited[nx][ny] = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0: continue
                visited = [[0] * m for _ in range(n)]
                visited[i][j] = 1
                go(i, j, visited, grid[i][j])
                visited[i][j] = 0
        return answer