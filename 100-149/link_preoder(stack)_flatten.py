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

        # 全局dummy
        # self.pointer = None
        # def traverse(root):
        #     if not root:return
        #     # 后序遍历
        #     traverse(root.right)
        #     traverse(root.left)
        #     root.left = self.pointer
        #     root.left = None
        #     self.pointer = root
        # traverse(root)

"""
public class Solution {
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public TreeNode parentNode = null;
    public void flatten(TreeNode root) {
        if (root == null){
            return;
        }
        if (parentNode != null){
            parentNode.left = null;
            parentNode.right = root;
        }
        # 后移不是next,而是后赋值前
        parentNode = root;
        flatten(root.left);
        flatten(root.right);
    }
}
"""





