class Solution:
	def reverseSubGroup(self, head, k=3):
		# 3 pointer approach for reversing linked list, prev, cur, nxt
		prev = head
		cur = head.next
		cur_k = 1

		# Iterate and reverse linked list
		while cur_k < k and cur:
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
			cur_k += 1

		# If the length of the sub-linked-list is smaller than k, then the order is meant to be left as it was
		# So, reverse the sub-linked-list we just reversed, pass in cur_k so it only attempts to reverse the number of nodes
		# we know are remaining
		if cur_k < k:
			head.next = None
			return self.reverseSubGroup(prev, cur_k)

		# start, end, next for reversed subgroup
		return prev, head, cur


	def reverseKGroup(self, head, k: int):
		# Reverse the first sub-linked-list separately to obtain a pointer to the new head of the linked list
		start, prev_end, nxt = self.reverseSubGroup(head, k)
		reversed_head = start

		# Reverse the remaining sub-linked-lists
		while nxt:
			start, end, nxt = self.reverseSubGroup(nxt, k)
			prev_end.next = start
			prev_end = end

		# Ensure the new last node of the linked list terminates the linked list
		prev_end.next = None
		return reversed_head

