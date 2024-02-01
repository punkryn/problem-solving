class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = 1, max(nums)
        n = len(nums)

        def deter(mid):
            cnt = 0
            flag = 0
            for i in range(n):
                if flag:
                    flag = 0
                    continue

                if nums[i] <= mid:
                    cnt += 1
                    flag = 1
            return cnt >= k
        
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            
            if deter(mid):
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans
                