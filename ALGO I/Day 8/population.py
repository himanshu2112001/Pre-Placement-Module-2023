class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root: return 
        
        q = deque([root])
        
        while q:
            qLen = len(q)
            for i in range(qLen):
                curr = q.popleft()
                if i < qLen-1:
                    curr.next = q[0]
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)                    
                    
        return root