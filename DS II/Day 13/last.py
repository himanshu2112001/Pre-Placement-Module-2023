from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        que = deque()
        while head:
            que.append(head)
            head = head.next
        res = []
        turn = True
        while que:
            if turn:
                res.append(que.popleft())
            else:
                res.append(que.pop())
            turn = not turn
        for x, y in zip(res,res[1:]):
            x.next= y
        if res: res[-1].next = None
        return res[0] if res else None

