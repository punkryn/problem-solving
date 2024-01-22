class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        
        total = n * (n - 1) // 2
        num_dict = defaultdict(int)

        for i in range(n):
            num = i - nums[i]            
            num_dict[num] += 1
        
        m = 0
        for v in num_dict.values():
            if v <= 1:
                continue
            m += v * (v - 1) // 2
        ans = total - m

        return ans