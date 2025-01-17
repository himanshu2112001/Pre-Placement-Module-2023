class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ///// In-place modification without extra space /////
        prev,cur = None,head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev