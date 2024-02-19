class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)

        if l >= len(nums) or nums[l] != target: return [-1, -1]

        return [l, r - 1]