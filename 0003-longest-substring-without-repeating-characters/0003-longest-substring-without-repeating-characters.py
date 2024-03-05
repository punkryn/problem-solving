class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        l = 0
        n = len(s)
        ans = 0
        for r in range(n):
            cur = s[r]
            if cur not in d:
                d[cur] = r
                ans = max(ans, r - l + 1)
                continue
            
            l = max(l, d[cur] + 1)
            d[cur] = r

            ans = max(ans, r - l + 1)
        return ans
            