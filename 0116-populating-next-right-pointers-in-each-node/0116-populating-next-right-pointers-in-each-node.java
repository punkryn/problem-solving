/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        if (root == null) {
            return root;
        }
        traversal(root);
        return root;
    }

    private void traversal(Node cur) {
        if (cur.left == null) {
            return;
        }

        List<Node> right = goRight(cur.left);
        List<Node> left = goLeft(cur.right);

        for (int i = 0; i < right.size(); i++) {
            right.get(i).next = left.get(i);
        }

        traversal(cur.left);
        traversal(cur.right);
    }

    private List<Node> goRight(Node cur) {
        if (cur.right == null) {
            List<Node> ret = new ArrayList<>();
            ret.add(cur);
            return ret;
        }

        List<Node> ret = goRight(cur.right);
        ret.add(cur);

        return ret;
    }

    private List<Node> goLeft(Node cur) {
        if (cur.left == null) {
            List<Node> ret = new ArrayList<>();
            ret.add(cur);
            return ret;
        }

        List<Node> ret = goLeft(cur.left);
        ret.add(cur);

        return ret;
    }
}