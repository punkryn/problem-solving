class Solution {
    public int countVowelStrings(int n) {
        int[] dp = new int[]{1, 1, 1, 1, 1};

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < 4; j++) {
                int sum = 0;
                for (int k = j; k < 5; k++) {
                    sum += dp[k];
                }
                dp[j] = sum;
            }
        }

        return Arrays.stream(dp).sum();
    }
}