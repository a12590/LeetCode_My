#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
newNode这里有什么用？
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        nodeDict = dict()
        dummy = RandomListNode(0)
        # head,dummy
        pointer,newHead = head,dummy
        # 遍历
        while pointer:
            newNode = RandomListNode(pointer.label)
            # .next 连接操作 / nodeDict 保存原pointer到newNode链接关系
            nodeDict[pointer] = newHead.next = newNode
            newHead,pointer = newHead.next,pointer.next
        # head,dummy
        pointer,newHead = head,dummy.next
        while pointer:
            if pointer.random:
                newHead.random = nodeDict[pointer.random]
            pointer,newHead = pointer.next,newHead.next
        return dummy.next

