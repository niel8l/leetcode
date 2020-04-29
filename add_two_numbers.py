# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        carry = 0
        dummy = current = ListNode(None)
        while p or q or carry:
            x = p and p.val or 0
            y = q and q.val or 0
            sum = x + y + carry
            carry, mod = divmod(sum, 10)
            current.val = mod
            p = p and p.next
            q = q and q.next
            if p or q or carry:
                current.next = ListNode(None)
                current = current.next
        return dummy
