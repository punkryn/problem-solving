class Solution {
    public boolean validateBinaryTreeNodes(int n, int[] leftChild, int[] rightChild) {
        int[] visited = new int[n];
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < n; i++) {
            int left = leftChild[i];
            int right = rightChild[i];

            if (left != -1 && visited[left] != 0) {
                return false;
            }

            if (right != -1 && visited[right] != 0) {
                return false;
            }

            if (left != -1) {
                visited[left] = 1;
                union(i, left, parent);
            }
            if (right != -1) {
                visited[right] = 1;
                union(i, right, parent);
            }
        }

        int prev = find(0, parent);
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i] == 0) {
                cnt += 1;
            }
            if (prev != find(i, parent)) {
                return false;
            }
        }

        if (cnt != 1) return false;
        return true;
    }

    private int find(int x, int[] parent) {
        if (x != parent[x]) {
            parent[x] = find(parent[x], parent);
        }
        return parent[x];
    }

    private void union(int x, int y, int[] parent) {
        x = find(x, parent);
        y = find(y, parent);

        if (x < y) {
            parent[y] = x;
        } else {
            parent[x] = y;
        }
    }
}