class Solution {
    public boolean checkMove(char[][] board, int rMove, int cMove, char color) {
        boolean ans = false;
        int n = board.length;
        int m = board[0].length;

        int[] dx = new int[]{-1, -1, 0, 1, 1, 1, 0, -1};
        int[] dy = new int[]{0, 1, 1, 1, 0, -1, -1, -1};
        char oppo = color == 'W' ? 'B' : 'W';
        for (int i = 0; i < 8; i++) {
            int nx = rMove + dx[i];
            int ny = cMove + dy[i];

            boolean oppoFlag = false;
            while (0 <= nx && nx < n && 0 <= ny && ny < m) {
                if (board[nx][ny] == '.') break;
                if (board[nx][ny] == oppo) {
                    oppoFlag = true;
                }

                if (board[nx][ny] == color && !oppoFlag) {
                    break;
                }

                if (board[nx][ny] == color && oppoFlag) {
                    return true;
                }

                nx += dx[i];
                ny += dy[i];
            }
        }
        return ans;
    }
}