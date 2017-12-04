#!/usr/bin/python
# _*_ coding: utf-8 _*_

""""
树先序遍历
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 初始化
        self.ans = 0x80000000
        # 最值套路
        MinVal = root.val
        # 树遍历
        def traverse(root):
            # 树遍历下套路
            if not root :return
            # 定势思维，这里不求最值，求倒数二值
            if self.ans > root.val > MinVal:
                self.ans = root.val
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return self.ans if self.ans != 0x80000000 else -1

if __name__ == '__main__' :
    solution = Solution()
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    print solution.findSecondMinimumValue(root)




