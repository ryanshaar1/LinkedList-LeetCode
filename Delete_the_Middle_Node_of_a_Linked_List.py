# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        pos = head
        pos2 = head
        count = 0
        while pos:
            count+=1
            pos = pos.next
        for i in range(count/2):
            if i+1 == count/2:
                pos2.next = pos2.next.next
            pos2 = pos2.next
        return head
            #I did this answer base on what i learned in high school but there is a more optimal way with two pointers.
        