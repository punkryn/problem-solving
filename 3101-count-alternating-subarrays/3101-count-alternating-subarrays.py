class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        group = []
        cnt = 1
        for i in range(1, n):
            if nums[i - 1] != nums[i]:
                cnt += 1
            else:
                group.append(cnt)
                cnt = 1
        
        group.append(cnt)
        
        ans = 0
        for c in group:
            ans += c * (c + 1) // 2
        
        return ans