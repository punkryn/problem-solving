class Solution {
    public int integerReplacement(int n) {
        Queue<Long> q = new LinkedList<>();
        Map<Long, Long> v = new HashMap<>();

        q.add((long)n);
        v.put((long)n, 0L);

        while (!q.isEmpty()) {
            long cur = q.poll();

            if (cur == 1) {
                long ret = v.get(cur);
                return (int)ret;
            }

            if (cur % 2 == 0) {
                long nxt = cur / 2;
                if (v.containsKey(nxt)) {
                    continue;
                }

                v.put(nxt, v.get(cur) + 1);
                q.add(nxt);
            } else {
                for (long d : new long[]{1, -1}) {
                    long nxt = cur + d;
                    if (v.containsKey(nxt)) continue;

                    v.put(nxt, v.get(cur) + 1);
                    q.add(nxt);
                }
            }
        }

        return 0;
    }
}