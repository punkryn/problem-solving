class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l = len(nums)

        e = 0
        target = sum(nums) - x
        cnt = -1
        cur = 0
        for s in range(l):
            while e < l and cur < target:
                cur += nums[e]
                e += 1
            
            if cur == target:
                cnt = max(cnt, e - s)
            
            cur -= nums[s]
        
        return l - cnt if cnt != -1 else -1