class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        r1 = [0] * n
        r2 = [0] * n

        r1[0] = grid[0][0]
        r2[0] = grid[1][0]
        for i in range(1, n):
            r1[i] = r1[i - 1] + grid[0][i]
            r2[i] = r2[i - 1] + grid[1][i]
        
        ans = float('inf')
        for i in range(n):
            ltor = i - 1
            rtol = i + 1

            tmp = 0
            if ltor >= 0:
                tmp = max(tmp, r2[ltor])
            
            if rtol < n:
                tmp = max(tmp, r1[n - 1] - r1[i])
            ans = min(ans, tmp)
        return ans