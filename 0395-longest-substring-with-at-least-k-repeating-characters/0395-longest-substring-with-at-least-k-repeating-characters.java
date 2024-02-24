class Solution {
    public int longestSubstring(String s, int k) {
        int n = s.length();
        if (n < k) return 0;

        return solution(s, k, 0, n - 1);
    }

    private int solution(String s, int k, int start, int end) {
        int n = s.length();
        boolean[] check = new boolean[n];
        Map<Character, Integer> counter = new HashMap<>();
        
        for (int i = start; i <= end; i++) {
            char cur = s.charAt(i);
            
            if (!counter.containsKey(cur)) {
                counter.put(cur, 0);
            }
            counter.put(cur, counter.get(cur) + 1);
        }

        Set<Character> deletedSet = new HashSet<>();
        for (char key : counter.keySet()) {
            int value = counter.get(key);
            if (value < k) {
                deletedSet.add(key);
            }
        }

        if (deletedSet.size() == 0) {
            return end - start + 1;
        }

        for (int i = start; i <= end; i++) {
            char cur = s.charAt(i);

            if (deletedSet.contains(cur)) {
                check[i] = true;
            }
        }

        int ans = 0;
        int l = start;
        boolean flag = true;
        boolean startFlag = false;
        for (int i = start; i <= end; i++) {
            if (check[i]) {
                flag = true;
                if (startFlag) {
                    ans = Math.max(ans, solution(s, k, l, i - 1));
                }

                startFlag = false;
                continue;
            }

            if (flag) {
                flag = false;
                startFlag = true;
                l = i;
            }
        }

        if (!check[end] && startFlag) {
            ans = Math.max(ans, solution(s, k, l, end));
        }

        return ans;
    }
}