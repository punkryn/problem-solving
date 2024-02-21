class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        ans = 0
        alpha = dict()
        for word in words:
            for a in word:
                if a not in alpha:
                    alpha[a] = 0
                alpha[a] += 1
        
        pairs = 0
        for cnt in alpha.values():
            pairs += cnt // 2
        
        for sz in sorted([len(word) for word in words]):
            pairs -= sz // 2
            if pairs < 0: break
            ans += 1
        return ans