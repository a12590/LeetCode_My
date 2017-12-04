#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
非递归先序遍历，注意rtype void要求
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # pointer
        pointer = TreeNode(None)
        if root is None:
            return
        stack = []
        stack.append(root)
        while stack:
            top = stack.pop()
            # 这里先遍历right是因为stack，使得出栈left先
            if top.right:
                stack.append(top.right)

            if top.left:
                stack.append(top.left)

            pointer.right = top
            pointer.left = None
            pointer = top




