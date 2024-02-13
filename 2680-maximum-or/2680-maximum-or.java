class Solution {
    public long maximumOr(int[] nums, int k) {
        int n = nums.length;
        if (n == 1) return nums[0] << k;
        
        long[] prefix = new long[n];
        prefix[0] = (long)nums[0];
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] | (long)nums[i];
        }

        long[] suffix = new long[n];
        suffix[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffix[i] = suffix[i + 1] | (long)nums[i];
        }

        long ans = Math.max(((long)nums[0] << k) | suffix[1], ((long)nums[n - 1] << k) | prefix[n - 2]);
        for (int i = 1; i < n - 1; i++) {
            ans = Math.max(ans, prefix[i - 1] | ((long)nums[i] << k) | suffix[i + 1]);
        }
        return ans;
    }
}