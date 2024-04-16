class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)

        tokens.sort()
        l, r = 0, n - 1

        ans = score = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1

                ans = max(ans, score)

                l += 1
            else:
                if score >= 1:
                    power += tokens[r]
                    score -= 1
                    r -= 1
                else:
                    break
        return ans