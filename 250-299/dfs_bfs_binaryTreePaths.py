#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
sum Path : 解题思路，dfs，核心：

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):

        """
        DFS
        """

        # self.ans = []
        # if root is None:
        #     return self.ans
        # def DFS(root,path):
        #     if root.left is None and root.right is None:
        #         # 这里把"1->3"和"1->2->5" 整个path append为结果
        #         # self.ans += path的话，会一串字符串
        #         self.ans.append(path)
        #     if root.left:
        #         # 这里默认更新path？
        #         DFS(root.left,path + "->" + str(root.left.val))
        #     if root.right:
        #         DFS(root.right,path + '->' + str(root.right.val))
        #
        # DFS(root,str(root.val))
        # return self.ans

        """
        BFS:TimeLimit
        """

        # from collections import deque
        # if root is None:
        #     return []
        # self.ans = []
        # def bfs(root,path):
        #     que = deque([root, str(root.val)])
        #     while que:
        #         if root.left is None and root.right is None:
        #             self.ans.append(path)
        #         if root.left:
        #             que += bfs(root.left,path + "->" + str(root.left.val))
        #         if root.right:
        #             que += bfs(root.right, path + "->" + str(root.right.val))
        # bfs(root,str(root.val))
        # return self.ans

        from collections import deque
        if root is None:
            return []
        # deque([root, str(root.val)]):
        que = deque([[root, str(root.val)]])
        ans = []
        while que:
            front,path = que.popleft()
            if front.left is None and front.right is None:
                ans.append(path)
            if front.left:
                # 队列 [ ]
                que += [front.left,path + "->" + str(front.left.val)]
            if front.right:
                que += [front.right, path + "->" + str(front.right.val)]
        return ans


"""
public class Solution {
    /**
     * @param root the root of the binary tree
     * @return all root-to-leaf paths
     */
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> rst = new ArrayList<String>();
        if (root == null){
            return rst;
        }

    }
    public void helper(TreeNode root,List<String> rst,ArrayList<Integer> list){
        list.add(root.val);
        if (root.left == null && root.right == null ){
            StringBuffer sb = new StringBuffer();
            for (int i = 0; i < list.size() - 1; i++){
                sb.append(list.get(i) + "->")
            }
            sb.append(list.get(list.size() - 1));
            rst.add(sb.toString());
        }
        if (root.left != null){
            helper(root.left,rst,list);
            # 出栈，pop 访问过了
            list.remove(list.size()-1);
        }
        if (root.right != null) {
    		helper(root.right, rst, list);
    		list.remove(list.size() - 1);
    	}
    }
}


"""