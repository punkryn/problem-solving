class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        dx = [1, -1, 0, 0, 0, 0]
        dy = [0, 0, 1, -1, 0, 0]
        dz = [0, 0, 0, 0, 1, -1]

        n = len(grid)

        v = [[[0] * 60 for _ in range(n + 2)] for _ in range(n + 2)]

        newMap = [[[0] * 60 for _ in range(n + 2)] for _ in range(n + 2)]
        
        for i in range(n):
            for j in range(n):
                for k in range(1, grid[i][j] + 1):
                    newMap[i + 1][j + 1][k] = 1

        q = deque()
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if newMap[i][j][1] == 1:
                    q.append((i, j, 1))
                    v[i][j][1] = 1
        
        def countSurface(x, y, z):
            ret = 0
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]

                if newMap[nx][ny][nz] == 0:
                    ret += 1
            return ret

        ans = 0
        while q:
            x, y, z = q.popleft()

            ans += countSurface(x, y, z)

            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                
                if v[nx][ny][nz] != 0:
                    continue

                if newMap[nx][ny][nz] == 0:
                    continue
                
                v[nx][ny][nz] = 1
                q.append((nx, ny, nz))
        return ans