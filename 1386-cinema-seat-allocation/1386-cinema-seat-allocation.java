class Solution {
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        Map<Integer, int[]> reservedRows = new HashMap<>();
        
        for (var seat : reservedSeats) {
            int r = seat[0], c = seat[1];
            
            if (!(reservedRows.containsKey(r))) {
                reservedRows.put(r, new int[11]);
            }
            reservedRows.get(r)[c] = 1;
        }

        int ans = 0;
        for (var row : reservedRows.keySet()) {
            var seats = reservedRows.get(row);
            if (check(seats, 2, 5)) {
                ans += 1;
                if (check(seats, 6, 9)) {
                    ans += 1;
                }
            } else {
                if (check(seats, 4, 7)) {
                    ans += 1;
                } else {
                    if (check(seats, 6, 9)) {
                        ans += 1;
                    }
                }
            }
        }

        return ans + (n - reservedRows.size()) * 2;
    }

    private boolean check(int[] seats, int x, int y) {
        for (int i = x; i <= y; i++) {
            if (seats[i] == 1) {
                return false;
            }
        }
        return true;
    }
}