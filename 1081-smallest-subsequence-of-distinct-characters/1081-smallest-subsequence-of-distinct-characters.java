class Solution {
    public String smallestSubsequence(String s) {
        Map<Character, Integer> hash = new HashMap<>();
        
        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            hash.put(cur, i);
        }

        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if (stack.search(cur) != -1) {
                continue;
            }
            
            while (!stack.isEmpty() && stack.peek() - 'a' > cur - 'a' && hash.get(stack.peek()) > i) {
                stack.pop();
            }
            stack.push(cur);
        }

        StringBuilder ans = new StringBuilder();
        while (!stack.isEmpty()) {
            char cur = stack.pop();
            ans.append(cur);
        }
        return ans.reverse().toString();
    }
}