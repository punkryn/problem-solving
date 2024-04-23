class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)

        MAX_LENGTH = int(1e5) * 2 + 10
        
        start = nums[0]
        
        ptrs = [0] * MAX_LENGTH

        for num in nums:
            ptrs[num] = 1
        ptr = start + 1

        prev = start
        ans = 0
        for i in range(1, n):
            if prev == nums[i]:
                while ptrs[ptr] == 1 or ptr <= nums[i]:
                    ptr += 1
                ptrs[ptr] = 1
                ans += ptr - nums[i]
            else:
                prev = nums[i]
        return ans