class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 10_001);
        dp[0] = 0;
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 1; j < Math.min(n - i, nums[i] + 1); j++) {
                dp[i + j] = Math.min(dp[i + j], dp[i] + 1);
            }
        }
        
        return dp[n - 1];
    }
}