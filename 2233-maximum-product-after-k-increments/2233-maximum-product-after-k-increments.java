class Solution {
    private final int mod = 1_000_000_007;
    public int maximumProduct(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((x, y) -> {
            if (x < y) return -1;
            if (x == y) return 0;
            return 1;
        });
        
        for (int num : nums) {
            pq.add(num);
        }

        for (int i = 0; i < k; i++) {
            int cur = pq.poll();
            pq.add(cur + 1);
        }

        long ans = 1;
        for (int num : pq) {
            ans = (ans * (long)num) % mod;
        }

        return (int)ans;
    }
}