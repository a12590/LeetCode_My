#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
动态规划：核心是存储+更新
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = max(nums)
        size = len(nums)
        # 这两个是list类型
        positive_max = [0 for x in range(size)]
        negative_min = [0 for x in range(size)]
        if nums[0] > 0:
            positive_max[0] = nums[0]
        else:
            negative_min[0] = nums[0]
        for x in range(1,size):
            if nums[x] > 0:
                positive_max[x] = max(nums[x],positive_max[x-1] * nums[x])
                # 连续 ，不是当前数，就是连续乘积
                negative_min[x] = negative_min[x-1] * nums[x]
            elif nums[x] < 0:
                positive_max[x] = negative_min[x-1] * nums[x]
                negative_min[x] = min(nums[x],positive_max[x-1] * nums[x])
            # 求ans 更新条件
            if positive_max[x] and positive_max[x] > ans:
                ans = positive_max[x]
        return ans


