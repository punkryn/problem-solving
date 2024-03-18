class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        r = 0
        n = len(nums)

        ans = 0
        curSum = 0
        curElement = set()
        for l in range(n):
            while r < n and r - l < k and nums[r] not in curElement:
                curSum += nums[r]
                curElement.add(nums[r])
                r += 1
            
            if r - l == k:
                ans = max(ans, curSum)
            
            curSum -= nums[l]
            curElement.remove(nums[l])
        return ans