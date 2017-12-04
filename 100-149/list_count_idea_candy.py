#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
画图，x-1 x x+1、左遍历，右遍历
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        size = len(ratings)
        candies = [1] * size
        for x in range(1,size):
            if ratings[x] > ratings[x-1]:
                candies[x] = candies[x-1] + 1
        # 反方向时，更新赋值需要考虑当前的值有可能更大
        for x in range(size - 2,-1,-1):
            if ratings[x] > ratings[x+1]:
                candies[x] = max(candies[x],candies[x+1]+1)
        return sum(candies)

if __name__ == '__main__':
    solution = Solution()
    print solution.candy([1,2,4,3])
