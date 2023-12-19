class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> ans = new ArrayList<int[]>();
        
        int newStart = newInterval[0], newEnd = newInterval[1];
        for (int[] interval : intervals) {
            int start = interval[0], end = interval[1];
            if (end < newStart) {
                ans.add(interval);
            } else if (newEnd < start) {
                ans.add(newInterval);
                newInterval = interval;
            } else {
                newInterval[0] = Math.min(newInterval[0], start);
                newInterval[1] = Math.max(newInterval[1], end);
            }
        }

        ans.add(newInterval);
        return ans.toArray(new int[ans.size()][]);
    }
}