#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
这里解释得很清楚：# 使用“哑节点”记录链表头部，dummy.next
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        # 使用“哑节点”记录链表头部
        dummy = ListNode(0)
        dummy.next = head
        # 使用pre, cur记录上一个元素和当前元素
        pre,cur = dummy,head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next
