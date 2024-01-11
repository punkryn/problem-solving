class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0: return False

        p = s // k

        if max(nums) > p: return False

        n = len(nums)
        nums.sort()
        
        dp = [False] * (1 << n)
        dp[0] = True
        total = [0] * (1 << n)

        for i in range(1 << n):
            if not dp[i]: continue
            for j in range(n):
                nxt = i | (1 << j)

                if nxt == i: continue

                if total[i] % p + nums[j] > p:
                    break
                
                dp[nxt] = True
                total[nxt] = total[i] + nums[j]
        
        return dp[(1 << n) - 1]