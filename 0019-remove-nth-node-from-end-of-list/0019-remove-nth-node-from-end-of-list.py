# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def go(cur, prev):
            nonlocal head
            if cur.next is None:

                if n == 1:
                    if prev is None:
                        head = None
                        return 1
                    prev.next = None
                return 1
            
            ret = 0
            ret += go(cur.next, cur) + 1
            if ret == n:
                if cur == head:
                    head = cur.next
                    return ret
                prev.next = cur.next
                return ret

            return ret
        
        go(head, None)
        return head