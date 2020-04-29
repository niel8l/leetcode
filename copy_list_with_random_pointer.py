# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        ni = {}
        i2rn = {}
        j = 0
        p = head
        arr = []
        while p:
            arr.append(Node(p.val))
            ni[p] = j
            if p.random:
                i2rn[j] = p.random
            p = p.next
            j += 1
        n = len(arr)
        for j in range(n):
            if j < n - 1:
                arr[j].next = arr[j+1]
            rn = i2rn.get(j)
            if rn is not None:
                arr[j].random = arr[ni[rn]]
        return arr[0]
