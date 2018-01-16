#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
单个（半边）
max(leftMax,rightMax,0) + root.val（要是root.val是负的呢？，没事，在下面ans跟新）

结合，而这里跟新ans
self.ans = max(max(leftMax,0)+max(rightMax,0) + root.val,self.ans)

# divide + Conquer思想
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
            # divide
            leftMax = search(root.left)
            rightMax = search(root.right)
            # 更新
            # Conquer
            self.ans = max(max(leftMax,0)+max(rightMax,0) + root.val,self.ans)
            # 出口2
            return max(leftMax,rightMax,0) + root.val
        search(root)
        return self.ans

"""
public class Solution{
    private class PathSumType{
        int singlePathMax;
        int combinedPathMax;
        PathSumType(int singlePathMax,int combinedPathMax){
            this.singlePathMax = singlePathMax;
            this.combinedPathMax = combinedPathMax;
        }
    }

    public int maxPathSum(TreeNode root){
        PathSumType result = helper(root);
        return result.combinedPathMax
    }
    public PathSumType helper(TreeNode root){
        if (root == null){
            return new PathSumType(0,Integer.MIN_VALUE);
        }
        PathSumType left = helper(root.left);
        PathSumType right = helper(root.right);
        # 单边：考虑0
        int singlePathMax = Math.max(left.singlePathMax,right.singlePathMax);
        singlePathMax = Math.max(singlePathMax,0);
        # 跟上面不同的是：上面 (0,left.singlePathMax)：可左可无
        # 这里好像有点问题啊：combinedPathMax做了一次更新，singlePathMax （一定要有吗？）
        int combinedPathMax = Math.max(left.combinedPathMax,right.combinedPathMax);
        combinedPathMax = Math.max(combinedPathMax,left.singlePathMax + right.singlePathMax + root.val);
        return new PathSumType(singlePathMax,combinedPathMax)
    }
}

"""

"""
本题是双边的

单边的
方法一：
public class Solution {
    public int maxPathSum2(TreeNode root) {
       if (root == null){
            return 0;
       }
       return dfs(root,0);
    }
    public int dfs (TreeNode node, int sum){
        if (node == null){
            return sum;
        }
        # 两种遍历方法，上面遍历单个，而跟新ans是从两边考虑
        # 这个是直接：左节点和当前的sum,右节点和sum，不考虑左右和sum
        # 这是两道题
        sum += node.val
        Math.max(Math.max(dfs(node.left, sum),dfs(node.right, sum)),sum)；
    }

}

方法二：想法更接近本题的
public class Solution{
    public int maxPathSum2(TreeNode root){
        if (root == null){
            return 0;
       }
       # 这部分不重复吗？
       int leftMax = helper(root.left)
       int rightMax = helper(root.right)
       # 没有0，应该内部比较过
       return Math.max(leftMax,rightMax) + root.val
    }
    public int helper(TreeNode node){
        # 出口比较过了
        if (node == null){
            return 0;
        } else if (node.left == null && node.right == null){
            return node.val > 0 ? node.val:0;
        }
        int leftMax = helper(root.left)
        int rightMax = helper(root.right)
        # 没有0，应该内部比较过
        int sum = Math.max(leftMax,rightMax) + root.val
        return sum > 0 ? sum : 0;
    }
}


"""


