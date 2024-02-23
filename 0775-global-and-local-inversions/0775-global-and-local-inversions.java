class Solution {
    public boolean isIdealPermutation(int[] nums) {
        int n = nums.length;

        int prev = -1;
        for (int i = 0; i < n - 2; i++) {
            prev = Math.max(prev, nums[i]);
            if (prev > nums[i + 2]) return false;
        }
        return true;
    }
}