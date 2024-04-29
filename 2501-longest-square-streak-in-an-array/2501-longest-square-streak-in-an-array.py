class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dp = [0] * 100_001

        num_set = set(nums)

        for num in nums:
            dp[num] = 1
        
        for i in range(2, 100_001):
            nxt = i * i
            if nxt > 100_000:
                break

            if i not in num_set:
                continue

            dp[nxt] = max(dp[nxt], dp[i] + 1)
        
        ans = -1
        for i in range(1, 100_001):
            if i in num_set and dp[i] > 1:
                ans = max(ans, dp[i])
        return ans