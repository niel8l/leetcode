# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = None
        for l in lists:
            head = self.mergeTwoLists(head, l)
        return head

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = current = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return head.next
