#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
java : 条件：isEmpty Stack List的定义，方法：push() ,pop(),null

preorder(stack(当前+right) or top(当前,一直left遍历))
postorder()
总感觉这块有点问题，就是先进后出，那么先出的是right，但是想遍历左树啊？
if cur.left:
    stack.append(cur.left)
elif cur.right:
    stack.append(cur.right)

    stack（None + pre是父节点，+ pre 是还是节点 => right（(pre == cur.left and cur.right:)）)

inorder(stack(一直left遍历并压栈直到null（进） + )  or top(当前（出），注意右遍历))

java:
1、 final List<List          new ArrayList<List<Integer>>();
2、 Queue<TreeNode>   = new LikedList<>();
函数 poll

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
                    stack.append(cur.right)
            elif pre == cur.left and cur.right:
                stack.append(cur.right)
            else:
                ans.append(cur.val)
                stack.pop()
            pre = cur
        return ans




