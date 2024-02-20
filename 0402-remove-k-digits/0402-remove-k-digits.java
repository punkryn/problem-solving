class Solution {
    public String removeKdigits(String num, int k) {
        if (num.length() <= k) return "0";

        Stack<Character> stack = new Stack<>();
        int n = num.length();
        for (int i = 0; i < n; i++) {
            char cur = num.charAt(i);
            if (stack.isEmpty()) {
                stack.push(cur);
                continue;
            }

            while (!stack.isEmpty() && stack.peek() > cur && k > 0) {
                stack.pop();
                k--;
            }

            stack.push(cur);
        }

        while (k > 0 && !stack.isEmpty()) {
            k--;
            stack.pop();
        }

        StringBuilder sb = new StringBuilder();
        for (var c : stack) {
            if (sb.length() == 0 && c == '0') continue;
            sb.append(c);
        }
        return sb.length() == 0 ? "0" : sb.toString();
    }
}