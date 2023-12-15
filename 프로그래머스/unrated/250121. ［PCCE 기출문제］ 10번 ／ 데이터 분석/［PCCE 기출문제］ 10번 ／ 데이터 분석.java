import java.util.*;


class Solution {
    private int getIndex(String ext) {
        if (ext.equals("code")) {
            return 0;       
        } else if (ext.equals("date")) {
            return 1;
        } else if (ext.equals("maximum")) {
            return 2;
        } else {
            return 3;
        }
    }
    public ArrayList<int[]> solution(int[][] data, String ext, int val_ext, String sort_by) {
        int[][] answer = {};
        
        ArrayList<int[]> arr = new ArrayList<int[]>();
        for (int[] d : data) {
            int idx = this.getIndex(ext);
            if (d[idx] < val_ext) {
                arr.add(d);
            }
        }
        
        int sortIdx = this.getIndex(sort_by);
        arr.sort(new Comparator<int[]>() {
            @Override
            public int compare(int[] i1, int[] i2) {
                return i1[sortIdx] - i2[sortIdx];
            }
        });
        
        return arr;
    }
}