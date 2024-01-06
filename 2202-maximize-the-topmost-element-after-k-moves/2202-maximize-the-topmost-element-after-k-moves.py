class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1 and k % 2 == 1:
            return -1
        
        if k == 0:
            return nums[0]

        if k == 1:
            return nums[1]
        
        if k < n:
            return max(max(nums[:k - 1]), nums[k])
        
        if k == n:
            return max(nums[:k - 1])

        return max(nums[:k])