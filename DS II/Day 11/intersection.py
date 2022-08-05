class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        pa, pb = headA, headB
        # Find the lengths of the two linked lists
        la, lb = 0, 0
        while pa:
            pa = pa.next
            la += 1
        while pb:
            pb = pb.next
            lb += 1
        
        pa, pb = headA, headB
        if la > lb:
            for _ in range(la-lb):
                pa = pa.next
        elif la < lb:
            for _ in range(lb-la):
                pb = pb.next
        for _ in range(min(la, lb)):
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next
        return None
