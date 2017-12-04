#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        # if root is None:
        #     return []
        # stack = [root]
        # ans = []
        # while stack:
        #     top = stack.pop()
        #     ans.append(top.val)
        #     if top.left:
        #         stack.append(top.left)
        #     if top.right:
        #         stack.append(top.right)
        # return ans[::-1]
        if root is None:
            return []
        stack = [root]
        ans = []
        pre = None
        while stack:
            cur = stack[-1]
            if pre is None or pre.left == cur or pre.right == cur:
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.left)
            elif pre == cur.left and cur.right:
                stack.append(cur.right)
            else:
                ans.append(cur.val)
                stack.pop()
            pre = cur
        return ans




