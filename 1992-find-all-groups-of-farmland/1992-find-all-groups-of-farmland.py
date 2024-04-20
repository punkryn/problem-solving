dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        return self.getGroups(land)

    def getGroups(self, land):
        n = len(land)
        m = len(land[0])

        groups = []

        visited = [[0] * m for _ in range(n)]
        cnt = 1
        for i in range(n):
            for j in range(m):
                if land[i][j] == 0: continue
                if visited[i][j] != 0: continue

                coordinate = self.dfs(land, visited, i, j, cnt)
                cnt += 1

                coordinate.sort()

                if self.isRect(coordinate):
                    groups.append([coordinate[0][0], coordinate[0][1], coordinate[-1][0], coordinate[-1][1]])
        return groups
                
    def dfs(self, land, visited, i, j, cnt):
        n = len(land)
        m = len(land[0])

        st = [(i, j)]
        visited[i][j] = 1

        coordinate = [(i, j)]
        while st:
            x, y = st.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if not (0 <= nx < n and 0 <= ny < m): continue
                if land[nx][ny] == 0: continue
                if visited[nx][ny] != 0: continue

                visited[nx][ny] = cnt
                st.append((nx, ny))
                coordinate.append((nx, ny))
        return coordinate
    
    def isRect(self, coord):
        minx, miny = min(coord, key=lambda x: x[0])[0], min(coord, key=lambda x: x[1])[1]
        maxx, maxy = max(coord, key=lambda x: x[0])[0], max(coord, key=lambda x: x[1])[1]

        if coord[0][0] == minx and coord[0][1] == miny and coord[-1][0] == maxx and coord[-1][1] == maxy:
            return True
        return False