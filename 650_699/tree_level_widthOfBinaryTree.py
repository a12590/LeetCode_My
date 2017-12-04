#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
二叉树层次遍历
对二叉树节点进行标号，根节点标号为1；
若某节点标号为c，则其左右孩子标号分别为2c, 2c + 1
某层的宽度即为最右、最左节点标号之差+1
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 层次遍历时候，依次增加的节点是排排坐即可
        # [(节点，值（这里是下标）),(),(),()...]
        q = [(root,1)]
        ans = 0
        # 层次遍历套路
        while q:
            width = q[-1][-1] - q[0][-1] + 1
            ans = max(ans,width)
            # 作用层次遍历中，一层一层而需要的
            q0 = []
            # if root.left:
            for n,i in q:
                if n.left: q0.append((n.left,i*2))
                if n.right:q0.append((n.right,i*2+1))
            q = q0
        return ans

if __name__ == '__main__' :
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(4)
    print solution.widthOfBinaryTree(root)
