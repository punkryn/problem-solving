class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        min1 = max(0, n - limit * 2)
        max1 = min(limit, n)
        for i in range(min1, max1 + 1):
            min2 = max(0, n - i - limit)
            max2 = min(limit, n - i)
            ans += max2 - min2 + 1
        return ans