#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
#cut in the mid(sortList中归并排序)
# reverse right half。
# 在就一句那会被破坏，故保存
# right和cursor遍历右移
# 区别于and。这里要来个判断
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None:
            return head
        mid = self.getMiddle(head)

        #cut in the mid(sortList中归并排序)
        left = head
        right = mid.next
        # 只有一个值
        if right is None:
            return head
        mid.next = None

        # reverse right half。
        cursor = right.next
        right.next = None
        while cursor:
            # 在就一句那会被破坏，故保存
            next = cursor.next
            # 就一句
            cursor.next = right
            # right和cursor遍历右移
            right = cursor
            cursor = next

        dummy = ListNode(0)
        # 二分
        while left or right:
            # 区别于and。这里要来个判断
            if left is not None:
                dummy.next = left
                # 遍历右移思想
                left = left.next
                dummy = dummy.next
            if right is not None:
                dummy.next = right
                right = right.next
                dummy = dummy.next
        return head

    # sortList中归并排序
    def getMiddle(self,head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

