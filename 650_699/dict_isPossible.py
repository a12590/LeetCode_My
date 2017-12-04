#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
Map + PriorityQueue
思路类似于排列扑克牌，优先将数字排在长度较小的扑克牌队列后面
Map<Integer, PriorityQueue<Integer>>
dmap的key为扑克牌队列的末尾，value为优先队列，存储扑克牌队列的长度
"""

import collections
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dmap = collections.defaultdict()
        def getOrPut(num):
            pq = dmap.get(num)
            if pq is None:
                dmap[num].set(pq)
            return pq
        for num in nums:
            pq0 = getOrPut(num - 1)
            print pq0
            # len =

if __name__ == '__main__' :
    solution = Solution()
    print solution.isPossible([1,2,3,3,4,5])
