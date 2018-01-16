#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
# 使用“哑节点”记录链表头部，dummy.next
思想：后N个，可以通过（距离为N）双指针从头到尾地遍历。
# why this action?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        # 使用“哑节点”记录链表头部
        dummy = ListNode(0)
        dummy.next = head
        # 使用pre, cur记录上一个元素和当前元素
        pre, cur = dummy, head

        # cur 走n步
        for i in range(n):
            cur = cur.next

        # 遍历
        while cur.next:
            pre = pre.next
            cur = cur.next

        # remove
        p =  pre.next
        pre.next = p.next

        # 应该可删可不删，释放空间
        del p
        # while cur:
        #     # if cur.val == val:
        #         pre.next = cur.next
        #     # else:
        #         pre = cur
        #     cur = cur.next
        return dummy.next