class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ho = [[0] * (m + 1) for _ in range(n + 1)]
        ve = [[0] * (m + 1) for _ in range(n + 1)]
    
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if grid[i - 1][j - 1] == 1:
                    ho[i][j] = ho[i][j - 1] + 1
                    ve[i][j] = ve[i - 1][j] + 1
        
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for k in range(min(i, j)):
                    if not (grid[i - 1][j - 1 - k] == 1 and grid[i - 1 - k][j - 1] == 1):
                        break
                    
                    if ve[i][j - k] > k and ho[i - k][j] > k:
                        ans = max(ans, (k + 1) ** 2)
        return ans