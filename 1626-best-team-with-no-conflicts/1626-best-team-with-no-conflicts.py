class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)

        sorted_ages = sorted([[age, i] for i, age in enumerate(ages)], key=lambda x: (x[0], scores[x[1]]))
        
        dp = [scores[sorted_ages[i][1]] for i in range(n)]
        ans = dp[0]
        for i in range(1, n):
            cur_score = scores[sorted_ages[i][1]]
            for j in range(i):
                score = scores[sorted_ages[j][1]]
                if score > cur_score:
                    continue
                dp[i] = max(dp[i], dp[j] + cur_score)
                
            ans = max(ans, dp[i])
        
        return ans