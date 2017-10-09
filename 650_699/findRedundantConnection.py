#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
利用数组degree记录各顶点的度。
利用数组neighbor记录各顶点的邻接顶点。
从度为1的节点出发进行拓扑排序，剩余边中在edges中排最后的那条即为答案。
"""

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

if __name__ == '__main__' :
    solution = Solution()
    print solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]])