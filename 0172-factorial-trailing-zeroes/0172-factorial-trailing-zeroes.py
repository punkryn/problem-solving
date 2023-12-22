class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        cur = 5
        while n // cur > 0:
            ans += n // cur
            cur *= 5

        return ans