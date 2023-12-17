/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeNodes(ListNode head) {
        ListNode cur = head.next;
        ListNode ans = new ListNode();
        ListNode ans_ptr = ans;
        
        int sum = 0;
        while (cur != null && cur.next != null) {
            if (cur.val == 0) {
                ans_ptr.val = sum;
                ans_ptr.next = new ListNode();
                ans_ptr = ans_ptr.next;
                sum = 0;
            }
            sum += cur.val;
            
            cur = cur.next;
        }

        if (sum != 0) {
            ans_ptr.val = sum;
        }

        return ans;
    }
}