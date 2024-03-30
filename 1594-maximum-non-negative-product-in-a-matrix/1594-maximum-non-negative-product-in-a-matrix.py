class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = int(1e9) + 7
        INVALID = 17
        n = len(grid)
        m = len(grid[0])
        dp = [[[INVALID] * 3 for _ in range(m + 1)] for _ in range(n + 1)]
        if grid[0][0] >= 0:
            dp[1][1][0] = grid[0][0]
        elif grid[0][0] == 0:
            dp[1][1][2] = 0
        else:
            dp[1][1][1] = grid[0][0]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == 1 and j == 1: continue
                if grid[i - 1][j - 1] < 0:
                    p1 = dp[i - 1][j][1] * grid[i - 1][j - 1] if dp[i - 1][j][1] != INVALID else INVALID
                    p2 = dp[i][j - 1][1] * grid[i - 1][j - 1] if dp[i][j - 1][1] != INVALID else INVALID
                    
                    if p1 == INVALID and p2 == INVALID:
                        dp[i][j][0] = INVALID
                    elif p1 == INVALID:
                        dp[i][j][0] = p2
                    elif p2 == INVALID:
                        dp[i][j][0] = p1
                    else:
                        dp[i][j][0] = max(p1, p2)

                    p1 = dp[i - 1][j][0] * grid[i - 1][j - 1] if dp[i - 1][j][0] != INVALID else INVALID
                    p2 = dp[i][j - 1][0] * grid[i - 1][j - 1] if dp[i][j - 1][0] != INVALID else INVALID

                    if p1 == INVALID and p2 == INVALID:
                        dp[i][j][1] = INVALID
                    elif p1 == INVALID:
                        dp[i][j][1] = p2
                    elif p2 == INVALID:
                        dp[i][j][1] = p1
                    else:
                        dp[i][j][1] = min(p1, p2)

                    if dp[i - 1][j][2] == 0 or dp[i][j - 1][2] == 0:
                        dp[i][j][2] = 0

                elif grid[i - 1][j - 1] == 0:
                    dp[i][j][2] = 0

                else:
                    p1 = dp[i - 1][j][0] * grid[i - 1][j - 1] if dp[i - 1][j][0] != INVALID else INVALID
                    p2 = dp[i][j - 1][0] * grid[i - 1][j - 1] if dp[i][j - 1][0] != INVALID else INVALID

                    if p1 == INVALID and p2 == INVALID:
                        dp[i][j][0] = INVALID
                    elif p1 == INVALID:
                        dp[i][j][0] = p2
                    elif p2 == INVALID:
                        dp[i][j][0] = p1
                    else:
                        dp[i][j][0] = max(p1, p2)

                    p1 = dp[i - 1][j][1] * grid[i - 1][j - 1] if dp[i - 1][j][1] != INVALID else INVALID
                    p2 = dp[i][j - 1][1] * grid[i - 1][j - 1] if dp[i][j - 1][1] != INVALID else INVALID

                    if p1 == INVALID and p2 == INVALID:
                        dp[i][j][1] = INVALID
                    elif p1 == INVALID:
                        dp[i][j][1] = p2
                    elif p2 == INVALID:
                        dp[i][j][1] = p1
                    else:
                        dp[i][j][1] = min(p1, p2)

                    if dp[i - 1][j][2] == 0 or dp[i][j - 1][2] == 0:
                        dp[i][j][2] = 0
        

        if dp[n][m][0] == INVALID:
            if dp[n][m][2] != INVALID:
                return 0
            return -1

        return dp[n][m][0] % MOD