class Solution {
    private int MOD = (int)1e9 + 7;
    public int numDecodings(String s) {
        if (s.charAt(0) == '0') {
            return 0;
        }
        s = '0' + s;
        int n = s.length();
        long[][][] dp = new long[n][2][10];
        dp[0][0][0] = 0; dp[0][1][0] = 1;

        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == '*') {
                for (int j = 1; j < 10; j++) {
                    for (int k = 0; k < 10; k++) {
                        dp[i][1][j] += (dp[i - 1][0][k] + dp[i - 1][1][k]) % MOD;
                    }
                }
                
                if (s.charAt(i - 1) == '*') {
                    for (int j = 1; j < 10; j++) {
                        dp[i][0][j] += dp[i - 1][1][1] % MOD;
                    }
                    for (int j = 1; j < 7; j++) {
                        dp[i][0][j] += dp[i - 1][1][2] % MOD;
                    }
                    continue;
                }

                if (s.charAt(i - 1) == '1') {
                    for (int j = 1; j < 10; j++) {
                        dp[i][0][j] += (dp[i - 1][1][1]) % MOD;
                    }
                    
                } else if (s.charAt(i - 1) == '2') {
                    for (int j = 1; j < 7; j++) {
                        dp[i][0][j] += (dp[i - 1][1][2]) % MOD;
                    }
                }
                continue;
            }
            

            // 현재 digit 0인 경우
            if (s.charAt(i) == '0') {
                dp[i][1][0] = 0;
                if (s.charAt(i - 1) == '*') {
                    dp[i][0][0] = (dp[i - 1][1][1] + dp[i - 1][1][2]) % MOD;
                    continue;
                }

                if (s.charAt(i - 1) == '1') {
                    dp[i][0][0] = dp[i - 1][1][1] % MOD;
                    continue;
                } else if (s.charAt(i - 1) == '2') {
                    dp[i][0][0] = dp[i - 1][1][2] % MOD;
                    continue;
                }
                continue;
            }

            // 현재 숫자가 * 아니고 0 아닌 경우 
            // 단독
            int cur_digit = Integer.parseInt("" + s.charAt(i));
            for (int j = 0; j < 10; j++) {
                dp[i][1][cur_digit] += (dp[i - 1][0][j] + dp[i - 1][1][j]) % MOD;
            }

            // 연결
            // 이전 숫자가 *인 경우
            if (s.charAt(i - 1) == '*') {
                dp[i][0][cur_digit] += dp[i - 1][1][1] % MOD;
                if (cur_digit <= 6) {
                    dp[i][0][cur_digit] += dp[i - 1][1][2] % MOD;
                }
            }

            // 이전 숫자가 1인 경우
            if (s.charAt(i - 1) == '1') {
                dp[i][0][cur_digit] += dp[i - 1][1][1] % MOD;
            }

            // 이전 숫자가 2인 경우
            if (s.charAt(i - 1) == '2') {
                if (cur_digit <= 6) {
                    dp[i][0][cur_digit] += dp[i - 1][1][2] % MOD;
                }
            }
        }

        long ans = 0;
        for (int i = 0; i < 10; i++) {
            ans = (ans + dp[n - 1][0][i] % MOD) % MOD;
            ans = (ans + dp[n - 1][1][i] % MOD) % MOD;
        }
        return (int)ans;
    }
}