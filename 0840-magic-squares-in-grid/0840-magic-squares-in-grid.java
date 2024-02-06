class Solution {
    public int numMagicSquaresInside(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;

        int[][] hor = new int[row + 2][col + 2];
        int[][] ver = new int[row + 2][col + 2];
        int[][] dia = new int[row + 2][col + 2];
        int[][] rdia = new int[row + 2][col + 2];

        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= col; j++) {
                hor[i][j] = hor[i][j - 1] + grid[i - 1][j - 1];
            }
        }

        for (int j = 1; j <= col; j++) {
            for (int i = 1; i <= row; i++) {
                ver[i][j] = ver[i - 1][j] + grid[i - 1][j - 1];
            }
        }

        for (int i = 1; i <= row; i++) {
            for (int j = 1; j <= row; j++) {
                dia[i][j] = dia[i - 1][j - 1] + grid[i - 1][j - 1];
            }
        }

        for (int i = 1; i <= row; i++) {
            for (int j = col; j > 0; j--) {
                rdia[i][j] = rdia[i - 1][j + 1] + grid[i - 1][j - 1];
            }
        }

        int ans = 0;
        for (int i = 3; i <= row; i++) {
            for (int j = 3; j <= col; j++) {
                int h = hor[i][j] - hor[i][j - 3];
                int v = ver[i][j] - ver[i - 3][j];
                int d = dia[i][j] - dia[i - 3][j - 3];
                if (h == v && v == d) {
                    int[] number = new int[10];
                    boolean flag = true;
                    for (int k = 1; k <= 2; k++) {
                        if (hor[i - k][j] - hor[i - k][j - 3] != h) {
                            flag = false;
                            break;
                        }

                        if (ver[i][j - k] - ver[i - 3][j - k] != v) {
                            flag = false;
                            break;
                        }
                    }
                    if (rdia[i][j - 2] - rdia[i - 3][j + 1] != d) {
                        flag = false;
                    }

                    for (int k = i - 2; k <= i; k++) {
                        for (int l = j - 2; l <= j; l++) {
                            if (grid[k - 1][l - 1] > 9 || grid[k - 1][l - 1] == 0) continue;
                            number[grid[k - 1][l - 1]]++;
                        }
                    }
                    for (int k = 1; k <= 9; k++) {
                        if (number[k] == 0) {
                            flag = false;
                            break;
                        }
                    }

                    if (flag) {
                        ans++;
                    }
                }
            }
        }
        return ans;
    }
}