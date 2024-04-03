class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        first = text.count(pattern[0])
        second = text.count(pattern[1])

        if pattern[0] == pattern[1]:
            return (first + 1) * first // 2
        
        n = len(text)
        ps1 = [0] * (n + 1)

        for i in range(1, n + 1):
            ps1[i] = ps1[i - 1] + (1 if text[i - 1] == pattern[0] else 0)

        ans = 0
        if first > second:
            for i in range(n):
                if text[i] == pattern[1]:
                    ans += ps1[i + 1]
            ans += ps1[-1]
        else:
            for i in range(n):
                if text[i] == pattern[1]:
                    ans += ps1[i + 1] + 1
        return ans