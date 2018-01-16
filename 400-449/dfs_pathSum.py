#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

"""
# TODO
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def traverse(root,val):
            if not root:return 0
            # TODO :这里就有问题了,
            res = (val == root.val)
            res += traverse(root.left,val - root.val)




"""
public class Solution{
    public List<List<Integer>> pathSum(TreeNode root, int sum){
        List<List<Integer>> rst = new ArrayList<List<Integer>>();
        if (root == null){
            return rst;
        }
        dfs(rst,new ArrayList<Integer>(),root,0,sum);
        return rst;
    }

    public void dfs(List<List<Integer>> rst,List<List<Integer>> list,TreeNode node, int add,int sum){
        list.add(node.val);
        # 叶子节点,出口
        if(node.left = null && node.right == null){
            if(add + node.val == sum){
                rst.add(new ArrayList<Integer>(list));
            }
            return ;
        }
        if (node.left != null){
            # node.left.val? ....
            dfs(rst,list,node.left,add + node.val,sum);
        }
    }
}


"""

"""
# rst list（跟新中删除.这里有些不懂）
# 遍历时的：初始值：root,root.val,target，更新：
# root.left,(root.val)sum + node.left.val,target
public class Solution{
    public List<List<Integer>> binaryTreepathSum(TreeNode root, int target){
        List<List<Integer>> rst = new ArrayList<List<Integer>>();
        if (root == null){
            return rst;
        }

    }
    public void dfs(List<List<Integer>> rst,List<List<Integer>> list,TreeNode node, int target,int sum){
        if (node.left == null && node.right == null){
            if (sum == target){
                rst.add(new ArrayList<Integer>(list));
            }
            return ;
        }
        if (node.left != null) {
            list.add(node.left.val);

        }
    }
}
"""