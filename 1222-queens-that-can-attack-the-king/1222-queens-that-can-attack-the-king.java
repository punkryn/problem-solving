class Solution {
    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        int xking = king[0], yking = king[1];
        
        List<List<Integer>> ans = new ArrayList<>();
        Set<List<Integer>> queens_set = new HashSet<>();
        for (var queen : queens) {
            List<Integer> cur_queen = new ArrayList<>();
            cur_queen.add(queen[0]); cur_queen.add(queen[1]);
            queens_set.add(cur_queen);
        }

        int[] dx = new int[]{-1, -1, 0, 1, 1, 1, 0, -1};
        int[] dy = new int[]{0, 1, 1, 1, 0, -1, -1, -1};
        for (int i = 0; i < 8; i++) {
            go(ans, dx[i], dy[i], queens_set, xking, yking);
        }
        
        return ans;
    }

    private void go(List<List<Integer>> ans, int dx, int dy, Set<List<Integer>> queens, int xking, int yking) {
        for (int i = 0; i < 7; i++) {
            int nx = xking + dx, ny = yking + dy;
            if (!(0 <= nx && nx < 8 && 0 <= ny && ny < 8)) break;
            
            List<Integer> cur_queen = new ArrayList<>();
            cur_queen.add(nx); cur_queen.add(ny);
            
            if (queens.contains(cur_queen)) {
                ans.add(cur_queen);
                break;
            }

            xking = nx; yking = ny;
        }
    }
}