class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes)
        if n == 1:
            return votes[0]

        m = len(votes[0])
        cnt = [[0] * 26 for _ in range(m)]

        for j in range(m):
            for i in range(n):
                cnt[j][ord(votes[i][j]) - ord('A')] += 1
    

        ans = ''
        selected = set()
        for i in range(m):
            maxValue = 0
            maxIdx = 0
            for j in range(26):
                if j in selected: continue
                curValue = 0
                curIdx = 0
                for k in range(m):
                    curValue += cnt[k][j] * (10 ** (26 * 3 - (k * 3)))
                curValue += (26 - j)

                if maxValue < curValue:
                    maxValue = curValue
                    maxIdx = j
            
            selected.add(maxIdx)
            ans += chr(ord('A') + maxIdx)
        return ans