# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        q = head.next
        while q:
            next = q.next
            q.next = p
            p = q
            if not next:
                break
            q = next
        head.next = None
        return q
