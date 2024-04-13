class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        prev = 0
        ans = []
        for w in word:
            d = int(w)
            
            cur = prev * 10 + d

            if cur % m == 0:
                ans.append(1)
                prev = 0
            else:
                ans.append(0)
                prev = cur % m
        return ans