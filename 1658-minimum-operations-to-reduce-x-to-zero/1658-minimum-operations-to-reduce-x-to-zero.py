class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l = len(nums)
        nums = nums + nums
        l2 = len(nums)

        e = 0
        ans = 100_001
        cur = 0
        for s in range(l2):
            while e < l2 and e - s < l and cur < x:
                cur += nums[e]
                e += 1
            

            if (s == 0 or (l > s > 0 and e >= l - 1) or s == l or (s > l and e == 2 * l - 1)) and e - s <= l and cur == x:
                ans = min(ans, e - s)
            
            cur -= nums[s]
        
        return ans if ans != 100_001 else -1