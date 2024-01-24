class Solution {
    public int largest1BorderedSquare(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        int[][] h = new int[n][m];
        int[][] v = new int[n][m];

        for (int i = 0; i < n; i++) {
            h[i][0] = grid[i][0];
            for (int j = 1; j < m; j++) {
                if (grid[i][j] == 1) {
                    h[i][j] = h[i][j - 1] + 1;
                }
            }
        }

        for (int j = 0; j < m; j++) {
            v[0][j] = grid[0][j];
            for (int i = 1; i < n; i++) {
                if (grid[i][j] == 1) {
                    v[i][j] = v[i - 1][j] + 1;
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 0) continue;

                int min_idx = Math.min(i, j) + 1;
                int cur_h = h[i][j];
                int cur_v = v[i][j];
                min_idx = Math.min(min_idx, cur_h);
                min_idx = Math.min(min_idx, cur_v);
                
                for (int k = 1; k <= min_idx; k++) {
                    int prev_v = v[i][j - k + 1];
                    int prev_h = h[i - k + 1][j];

                    if (prev_v >= k && prev_h >= k) {
                        ans = Math.max(ans, k * k);
                    }
                }
            }
        }

        return ans;
    }
}