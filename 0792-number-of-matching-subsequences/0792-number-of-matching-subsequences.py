class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        alpha_idx = dict()

        for i, alpha in enumerate(s):
            if alpha not in alpha_idx:
                alpha_idx[alpha] = []
            alpha_idx[alpha].append(i)
        
        ans = 0
        for word in words:
            idx = 0
            for alpha in word:
                if alpha not in alpha_idx:
                    break

                iidx = bisect_left(alpha_idx[alpha], idx)
                if iidx >= len(alpha_idx[alpha]):
                    break
                
                idx = alpha_idx[alpha][iidx] + 1
            else:
                ans += 1
        return ans