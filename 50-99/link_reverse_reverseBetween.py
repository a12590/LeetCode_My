#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
# 我的版本
        def reverse(head):
            while head:
                p = head.next
                head.next = None
                p.next = head
                head = p

# 给出的版本，这个的好处一旦复杂，不乱
def reverse2(head):
    # 就使用 while p
    p = head
    # 加了个结果指针
    start = None
    while p:
        next = p.next
        p.next = start
        start = p
        p = next
    return start
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummyNode = ListNode(None)
        # 这是前后一对
        p = dummyNode
        q = head
        for x in range(m-1):
            p.next = q
            p = p.next
            q = q.next

        # start:结果指针、next:保存下一个，这是前后一对
        start = None
        next = None

        # end 保存逆置链最后一个节点，常用的方法
        end = q
        for x in range(m,n+1):
            next = q.next
            q.next = start
            start = q
            q = next

        # start:结果指针、next:保存下一个，这是前后一对
        p.next = start
        end.next = next
        return dummyNode.next



