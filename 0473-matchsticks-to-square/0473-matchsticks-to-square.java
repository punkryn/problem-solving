class Solution {
    public boolean makesquare(int[] matchsticks) {
        int n = matchsticks.length;
        if (n < 4) return false;

        int sum = Arrays.stream(matchsticks).sum();
        if (sum % 4 != 0) return false;

        int target = sum / 4;
        Arrays.sort(matchsticks);
        if (matchsticks[n - 1] != target && matchsticks[n - 1] + matchsticks[0] > target) {
            return false;
        }

        int[] visited = new int[n];
        return go(0, 0, 0, visited, target, matchsticks);
    }

    private boolean go(int depth, int cur, int idx, int[] visited, int target, int[] arr) {
        if (depth == 4) {
            if (visited.length == Arrays.stream(visited).sum()) {
                return true;
            }
            return false;
        }

        boolean ret = false;
        for (int i = idx; i < arr.length; i++) {
            if (visited[i] == 1) continue;
            int nxt = cur + arr[i];
            if (nxt > target) return false;
            if (nxt < target) {
                visited[i] = 1;
                ret |= go(depth, nxt, i + 1, visited, target, arr);
                if (ret) return ret;
                visited[i] = 0;
                continue;
            }

            visited[i] = 1;
            ret |= go(depth + 1, 0, 0, visited, target, arr);
            if (ret) return ret;
            visited[i] = 0;
        }
        return ret;
    }
}