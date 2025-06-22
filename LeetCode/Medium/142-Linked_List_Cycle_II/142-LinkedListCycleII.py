# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = h = head

        while h and h.next:
            if h.next:
                h = h.next.next
            t = t.next

            if h == t:
                break

        if not (h and h.next):
            return None

        t = head

        while t != h:
            t = t.next
            h = h.next

        return t
