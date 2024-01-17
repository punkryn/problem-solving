# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        cur = head
        size = 0 if cur is None else 1

        while cur.next is not None:
            size += 1
            cur = cur.next
        
        last_node = cur

        if size == 1:
            return head

        cnt = k % size
        if cnt == 0:
            return head
        
        cur = head
        
        target = size - cnt
        idx = 0
        
        while idx < target:
            if idx + 1 == target:
                nxt = cur.next

                tmp_head = head
                head = nxt

                cur.next = None

                last_node.next = tmp_head
                break

            cur = cur.next
            idx += 1

        return head