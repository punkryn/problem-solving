class Solution {
    private record Comb(int val, int i, int j) {}
    private record Indice(int w, int x, int y, int z) {}
    public List<List<Integer>> fourSum(int[] nums, int target) {
        int n = nums.length;
        Arrays.sort(nums);

        Set<Indice> ans = new HashSet<>();
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    long sum = (long)nums[i] + (long)nums[j] + (long)nums[k];
                    if (sum > Integer.MAX_VALUE) continue;
                    if (sum < Integer.MIN_VALUE) continue;
                    
                    int x = target - (int)sum;
                    int idx = Arrays.binarySearch(nums, k + 1, n, x);
                    if (idx < 0) continue;
                    ans.add(new Indice(nums[i], nums[j], nums[k], nums[idx]));
                }
            }
        }

        List<List<Integer>> ret = new ArrayList<>();
        for (var a : ans) {
            ret.add(new ArrayList<Integer>(
                Arrays.asList(a.w, a.x, a.y, a.z)
            ));
        }
        return ret;
    }
}