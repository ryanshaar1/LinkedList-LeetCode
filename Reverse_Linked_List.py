# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        
        node = None
        pos = head
        while pos:
            nodeN = ListNode(pos.val)
            nodeN.next = node
            node = nodeN
            pos = pos.next
        return node
