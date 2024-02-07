class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1];
        dp[0] = 1;
        
        for (int i = 0; i < target; i++ ) {
            for (int num : nums) {
                int nxt = num + i;
                if (nxt > target) continue;
                dp[nxt] += dp[i];
            }
        }
        return dp[target];
    }
}