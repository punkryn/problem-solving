class RangeFreqQuery {
    private final Map<Integer, ArrayList<Integer>> hash = new HashMap<>();
    public RangeFreqQuery(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (!hash.containsKey(arr[i])) {
                hash.put(arr[i], new ArrayList<>());
            }
            hash.get(arr[i]).add(i);
        }
    }
    
    public int query(int left, int right, int value) {
        if (!hash.containsKey(value)) {
            return 0;
        }

        int l = lowerBound(left, hash.get(value));
        int r = upperBound(right, hash.get(value));

        // System.out.println("" + l + ", " + r);

        return r - l;
    }

    private int lowerBound(int x, ArrayList<Integer> arr) {
        int l = 0, r = arr.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (arr.get(mid) < x) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }

    private int upperBound(int x, ArrayList<Integer> arr) {
        int l = 0, r = arr.size();
        while (l < r) {
            int mid = (l + r) / 2;
            if (arr.get(mid) <= x) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l;
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery obj = new RangeFreqQuery(arr);
 * int param_1 = obj.query(left,right,value);
 */