#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
# 为什么是last 和 head 比较
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        # get the middle
        mid = self.getMiddle(head)
        # reverse right half。
        p = mid.next
        last = None
        # mid.next = None
        while p:
            # 在就一句那会被破坏，故保存
            next = p.next
            # 就一句
            p.next = last
            # last和p遍历右移
            last = p
            p = next

        # 这里才到isPalindrome
        p1,p2 = last,head
        while p1 and p1.val == p2.val:
            p1,p2 = p1.next,p2.next

        # #resume linked list(optional)
        p, last = last, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        mid.next = last
        return p1 is None

    def getMiddle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow