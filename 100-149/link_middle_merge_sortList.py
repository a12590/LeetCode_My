#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        mid = self.getMiddle(head)
        rHead = mid.next
        mid.next = None
        return self.merge(self.sortList(head),self.sortList(rHead))

    def merge(self,lHead,rHead):
        # 细节：dummyNode
        dummyNode = ListNode(0)
        dummyHead = dummyNode
        while lHead and rHead:
            if lHead.val < rHead.val:
                dummyHead.next = lHead
                lHead = lHead.next
            else:
                dummyHead.next = rHead
                rHead = rHead.next
            dummyHead = dummyHead.next
        if lHead:
            dummyHead.next = lHead
        elif rHead:
            dummyHead.next = rHead
        return dummyNode.next

    def getMiddle(self,head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


