#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
任意节点只能出现一次。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = None
        def search(root):
            # 出口1
            if root is None:
                return 0
            leftMax = search(root.left)
            rightMax = search(root.right)
            # 更新
            self.ans = max(max(leftMax,0)+max(rightMax,0) + root.val,self.ans)
            # 出口2
            return max(leftMax,rightMax,0) + root.val
        search(root)
        return self.ans
