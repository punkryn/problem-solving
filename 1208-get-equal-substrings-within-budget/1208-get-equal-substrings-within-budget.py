class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        r = 0
        n = len(s)
        curCost = 0
        ans = 0
        for l in range(n):
            while r < n and curCost + abs(ord(s[r]) - ord(t[r])) <= maxCost:
                curCost = curCost + abs(ord(s[r]) - ord(t[r]))

                r += 1
                
            ans = max(ans, r - l)
            curCost -= abs(ord(s[l]) - ord(t[l]))
        return ans