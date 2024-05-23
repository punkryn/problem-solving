class Solution:
    ans = 0
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mbo = 0
        for num in nums:
            mbo |= num
        
        n = len(nums)
        def go(depth, cur):
            if cur > mbo:
                return
            
            if cur == mbo:
                self.ans += 1
            
            for i in range(depth + 1, n):
                go(i, cur | nums[i])
        
        go(-1, 0)
        return self.ans
