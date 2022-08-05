class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        senital = ListNode(0,head)
        prev = senital
        while prev.next and prev.next.next:
            fn = prev.next
            sn = prev.next.next
            fn.next = sn.next
            prev.next = sn
            prev.next.next = fn
            prev = prev.next.next
        return senital.next

