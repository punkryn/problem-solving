class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = int(1e9) + 7

        dp = [[0] * 5 for _ in range(2)]
        for i in range(5):
            dp[0][i] = 1
        
        s = [[1, 2, 4], [0, 2], [1, 3], [2], [2, 3]]

        flag = False
        for i in range(2, n + 1):
            for j in range(5):
                tmp = 0
                if not flag:
                    for idx in s[j]:
                        tmp += dp[0][idx]

                    dp[1][j] = tmp % MOD
                else:
                    for idx in s[j]:
                        tmp += dp[1][idx]

                    dp[0][j] = tmp % MOD
            flag = not flag
        
        return sum(dp[(n + 1) % 2]) % MOD