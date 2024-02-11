class Solution {
    private record E(String x, int cnt) {}
    public int minMutation(String startGene, String endGene, String[] bank) {
        if (bank.length == 0) return -1;
        
        Set<String> bankSet = new HashSet<>();
        for (String mutation : bank) {
            bankSet.add(mutation);
        }

        Character[] cand = new Character[]{'A', 'C', 'G', 'T'};

        Queue<E> q = new LinkedList<>();
        q.add(new E(startGene, 0));

        Set<String> visited = new HashSet<>();
        visited.add(startGene);

        int ans = 0;
        while (!q.isEmpty()) {
            E cur = q.poll();
            
            if (cur.x.equals(endGene)) {
                return cur.cnt;
            }

            for (int i = 0; i < 8; i++) {
                for (Character c : cand) {
                    StringBuilder sb = new StringBuilder(cur.x);
                    sb.setCharAt(i, c);
                    String nxt = sb.toString();

                    if (visited.contains(nxt)) continue;
                    if (!bankSet.contains(nxt)) continue;

                    bankSet.remove(nxt);
                    visited.add(nxt);
                    q.add(new E(nxt, cur.cnt + 1));
                }
            }
        }

        return -1;
    }
}