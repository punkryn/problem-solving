class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        max_idx = 0
        for i in range(n):
            if i > max_idx:
                break
            if max_idx >= n - 1:
                break
            
            nxt = i + nums[i]
            max_idx = max(max_idx, nxt)
        
        return True if max_idx >= n - 1 else False