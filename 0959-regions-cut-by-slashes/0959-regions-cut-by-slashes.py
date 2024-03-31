class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        n = len(grid)
        m = len(grid[0])

        g = [[0] * (3 * m) for _ in range(3 * n)]

        for i in range(n):
            for j in range(m):
                l = grid[i][j]

                if l == '/':
                    g[i * 3][j * 3 + 2] = 1
                    g[i * 3 + 1][j * 3 + 1] = 1
                    g[i * 3 + 2][j * 3] = 1
                elif l == '\\':
                    g[i * 3][j * 3] = 1
                    g[i * 3 + 1][j * 3 + 1] = 1
                    g[i * 3 + 2][j * 3 + 2] = 1
        
        v = [[0] * (3 * m) for _ in range(3 * n)]
        ans = 0

        def bfs(x, y):
            q = deque([(x, y)])
            v[x][y] = 1

            while q:
                x, y = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if not (0 <= nx < n * 3 and 0 <= ny < m * 3):
                        continue
                    if v[nx][ny] != 0: continue
                    if g[nx][ny] == 1: continue

                    v[nx][ny] = ans
                    q.append((nx, ny))


        for i in range(n * 3):
            for j in range(m * 3):
                if g[i][j] == 1: continue
                if v[i][j] != 0: continue

                ans += 1
                bfs(i, j)
        
        # for i in range(n * 3):
        #     for j in range(m * 3):
        #         print(v[i][j], end=' ')
        #     print()
        # print()

        return ans