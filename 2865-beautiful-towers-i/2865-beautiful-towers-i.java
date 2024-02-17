class Solution {
    public long maximumSumOfHeights(List<Integer> maxHeights) {
        int n = maxHeights.size();

        long ans = 0;
        for (int i = 0; i < n; i++) {
            long sum = maxHeights.get(i);
            
            int prev = maxHeights.get(i);
            for (int j = i - 1; j >= 0; j--) {
                int height = Math.min(maxHeights.get(j), prev);
                sum += (long)height;
                prev = height;
            }

            prev = maxHeights.get(i);
            for (int j = i + 1; j < n; j++) {
                int height = Math.min(maxHeights.get(j), prev);
                sum += (long)height;
                prev = height;
            }

            ans = Math.max(ans, sum);
        }
        return ans;
    }
}