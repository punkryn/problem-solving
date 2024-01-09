class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        l = dict()
        r = dict()
        n = len(s)
        for i in range(n):
            if s[i] not in l:
                l[s[i]] = i
                r[s[i]] = i
                continue
            
            r[s[i]] = i
        
        ans = 0
        for k in l:
            ans += len(set(s[l[k] + 1: r[k]]))
        return ans