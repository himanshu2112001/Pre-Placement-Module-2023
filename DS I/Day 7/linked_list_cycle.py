class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next            
            if slow == fast:
                return True
        
        return False