class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left_cnt = [0] * n
        right_cnt = [0] * n

        cur_cnt = 0
        for i in range(n):
            if nums[i] % 2 == 0:
                cur_cnt += 1
            else:
                left_cnt[i] = cur_cnt
                cur_cnt = 0
        
        cur_cnt = 0
        for i in range(n - 1, -1, -1):
            if nums[i] % 2 == 0:
                cur_cnt += 1
            else:
                right_cnt[i] = cur_cnt
                cur_cnt = 0
        
        ans = 0
        r = 0
        odd_cnt = 0
        for l in range(n):
            while r < n and odd_cnt < k:
                if nums[r] % 2 == 1:
                    odd_cnt += 1
                r += 1
            
            if nums[l] % 2 == 1:
                if odd_cnt == k:
                    ans += (left_cnt[l] + 1) * (right_cnt[r - 1] + 1)

                odd_cnt -= 1
        return ans