class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)

        def deter(mid):
            SUM = 0
            for num in nums:
                SUM += math.ceil(num / mid)
            return SUM <= threshold

        ans = 1
        while l <= r:
            mid = (l + r) // 2
            
            if deter(mid):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans