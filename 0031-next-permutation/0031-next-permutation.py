class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        idx = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] <= nums[i - 1]:
                continue
            idx = i
            break
        
        if idx == 0:
            nums.sort()
            return
        
        idx -= 1
        idx2 = 0
        max_min_value = float('inf')
        for i in range(idx + 1, len(nums)):
            if nums[idx] < nums[i] and max_min_value > nums[i]:
                max_min_value = nums[i]
                idx2 = i
        
        nums[idx], nums[idx2] = nums[idx2], nums[idx]
        
        nums[idx + 1:] = sorted(nums[idx + 1:])