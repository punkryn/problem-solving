class Solution:
    def jump(self, nums: List[int]) -> int:
        INF = float('inf')
        n = len(nums)
        dp = [INF] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            for j in range(1, min(nums[i] + 1, n - i)):
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[n - 1]