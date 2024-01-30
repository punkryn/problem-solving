class Solution {
    public int maxRotateFunction(int[] nums) {
        int n = nums.length;

        int sum = Arrays.stream(nums).sum();

        int prev = 0;
        for (int i = 0; i < n; i++) {
            prev += nums[i] * i;
        }

        int ans = prev;
        for (int i = 1; i < n; i++) {
            int nxt = prev - (sum - nums[i - 1]) + nums[i - 1] * (n - 1);

            ans = Math.max(ans, nxt);

            prev = nxt;            
        }

        return ans;
    }
}