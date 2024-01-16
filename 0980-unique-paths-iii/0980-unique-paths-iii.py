dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        total_cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == -1:
                    continue
                total_cnt += 1
        
        sx, sy = 0, 0
        ex, ey = 0, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    sx, sy = i, j
                
                if grid[i][j] == 2:
                    ex, ey = i, j

        v = [[False] * m for _ in range(n)]
        
        def go(x, y, d, cnt):
            if grid[x][y] == 2:
                if cnt == total_cnt:
                    return 1
                return 0
            
            if not check(x, y):
                return 0

            ret = 0
            for i in range(4):
                if (i + 2) % 4 == d:
                    continue
                
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                
                if v[nx][ny]:
                    continue
                
                if grid[nx][ny] == -1:
                    continue
                
                v[nx][ny] = True
                ret += go(nx, ny, i, cnt + 1)
                v[nx][ny] = False
            return ret
        
        def check(x, y):
            ret = False
            for i in range(4):
                nex = ex + dx[i]
                ney = ey + dy[i]

                if x == nex and y == ney:
                    return True

                if not (0 <= nex < n and 0 <= ney < m):
                    continue
                
                if v[nex][ney] or grid[nex][ney] == -1:
                    continue
                ret |= True
            return ret
        
        v[sx][sy] = True
        return go(sx, sy, -1, 1)