class Solution(object):
    def removeNthFromEnd(self, head, n):
        headSize = 0
        
        # get the size of list
        current = head
        while current: 
            headSize += 1
            current = current.next
        
        # corner case of removing first node
        if n==headSize:
            return head.next
        
        # remove node from list
        current = head
        for i in range(headSize - n -1):
            current = current.next
        current.next = current.next.next
        
        return head