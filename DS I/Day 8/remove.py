class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head=head
        if self.head==None:
            return
        temp=self.head
        self.l=[]
        self.l.append(temp.val)
        while temp.next!=None:
            if temp.next.val in self.l:
                temp.next=temp.next.next
                continue
            else:
                self.l.append(temp.next.val)
            temp=temp.next
        return self.head
