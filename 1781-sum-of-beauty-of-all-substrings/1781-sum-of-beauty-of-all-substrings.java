class Solution {
    public int beautySum(String s) {
        int ans = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            Map<Character, Integer> map = new HashMap<>();
            if (!map.containsKey(s.charAt(i))) {
                map.put(s.charAt(i), 0);
            }
            map.put(s.charAt(i), map.get(s.charAt(i)) + 1);
            for (int j = i + 1; j < s.length(); j++) {
                Character cur_char = s.charAt(j);
                if (!map.containsKey(cur_char)) {
                    map.put(cur_char, 0);
                }
                map.put(cur_char, map.get(cur_char) + 1);

                int max = 0, min = 50000;
                for (int v : map.values()) {
                    max = Math.max(max, v);
                    min = Math.min(min, v);
                }
                ans += max - min;
            }
        }
        return ans;
    }
}