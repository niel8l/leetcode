# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        a = head
        b = head.next
        if not b:
            return head
        while True:
            if a.val == b.val:
                a.next = b.next
                b = b.next
            else:
                a = b
                b = b.next
            if not b:
                return head
