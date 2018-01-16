#!/usr/bin/python
# _*_ coding: utf-8 _*_

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        if lenA == 0 or lenB == 0:
            return None
        endA = self.getListEnd(headA)
        # endB = self.getListEnd(headB)
        # TODO：在这里连起来了，厉害了
        endA.next = headB
        hasCircle = False
        p = headA
        cnt = 0
        while p:
            cnt += 1
            if cnt > lenA + lenB:
                hasCircle = True
                break
            p = p.next
        if not hasCircle:
            endA.next = None
            return None
        p1 = headA
        for x in range(lenB):
            p1 = p1.next
        p2 = headA
        # 通过这种方式解决长度不同问题
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        endA.next = None
        return p1

    def getListEnd(self,head):
        end = head
        while end.next:
            end = end.next
        return end

    def getListLen(self,head):
        size = 0
        p = head
        while p:
            size += 1
            p = p.next
        return size

"""
public class Solution{
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null
        }
        int countA = getListLen(headA);
        int countB = getListLen(headB);

        # 长度不同问题：
        # node 长的链表，走了diff步
        diff = Math.abs(countA - countB);
        node = (countA > countB) ? headA:headB;
        while(diff != 0){
            diff--;
            node = node.next;
        }
        # headA:长，则改为node
        # headB：长，则改为node
        ListNode nodeA = (countA > countB)? node:headA;
        ListNode nodeB = (countA > countB)? headB:node
        while(nodeA != null && nodeB != null){
            if(nodeA == nodeB){
                return nodeA;
            }
        }
    }

    public int getListLen(ListNode head){
        int size = 0;
        TreeNode p = head;
        while(p != null){
            size ++;
            p = p.next;
        }
    }
}

"""