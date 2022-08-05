class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1,n2="",""
        while l1:
            n1=str(l1.val)+n1
            l1=l1.next
        while l2:
            n2=str(l2.val)+n2
            l2=l2.next
        
        total=int(n1)+int(n2)
        dummy=d=ListNode()
        
        for i in reversed(str(total)):
            d.next=ListNode(int(i))
            d=d.next
        return dummy.next
