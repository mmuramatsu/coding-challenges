# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        t = h = head

        while t and h and h.next:
            if h.next:
                h = h.next.next
            t = t.next

            if h == t:
                return True

        return False
