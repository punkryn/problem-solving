class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = int(1e9) + 7
        total_sum = sum(arr)
        
        arr = arr + (arr if k > 1 else [])
        n = len(arr)
        
        dp = [0 for _ in range(n)]
        dp[0] = arr[0]

        ans = max(0, dp[0])
        for i in range(1, n):
            dp[i] = max(dp[i - 1], arr[i - 1]) + arr[i]
            ans = max(ans, dp[i], arr[i])

        ans %= MOD
        if total_sum > 0 and k > 1:
            for i in range(k - 2):
                ans = (ans + total_sum) % MOD

        return ans