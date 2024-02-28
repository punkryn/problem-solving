class Solution {
    public boolean canReorderDoubled(int[] arr) {
        Map<Integer, Integer> set = new HashMap<>();
        Arrays.sort(arr);

        int n = arr.length;
        int idx = n;
        for (int i = 0; i < n; i++) {
            if (arr[i] >= 0) {
                idx = i;
                if (idx % 2 != 0) return false;
                break;
            }
        }

        for (int i = idx - 1; i >= 0; i -= 1) {
            if (set.containsKey(arr[i])) {
                set.put(arr[i], set.get(arr[i]) - 1);
                if (set.get(arr[i]) == 0) {
                    set.remove(arr[i]);
                }
                continue;
            }

            if (!set.containsKey(arr[i] * 2)) {
                set.put(arr[i] * 2, 0);
            }

            set.put(arr[i] * 2, set.get(arr[i] * 2) + 1);
        }

        for (var key : set.keySet()) {
            if (set.get(key) != 0) return false;
        }

        for (int i = idx; i < n; i += 1) {
            if (arr[i] == 0) {
                if (!set.containsKey(arr[i])) {
                    set.put(arr[i] * 2, 1);
                } else {
                    set.put(arr[i], set.get(arr[i]) - 1);
                    if (set.get(arr[i]) == 0) {
                        set.remove(arr[i]);
                    }
                }
                continue;
            }

            if (set.containsKey(arr[i])) {
                set.put(arr[i], set.get(arr[i]) - 1);
                if (set.get(arr[i]) == 0) {
                    set.remove(arr[i]);
                }
                continue;
            }

            if (!set.containsKey(arr[i] * 2)) {
                set.put(arr[i] * 2, 0);
            }

            set.put(arr[i] * 2, set.get(arr[i] * 2) + 1);
        }

        for (var key : set.keySet()) {
            if (set.get(key) != 0) return false;
        }

        return true;
    }
}