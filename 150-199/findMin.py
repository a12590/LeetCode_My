#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
二分法是一个条件吗？nums[high] >= nums[mid]:
注意这里的nums不允许重复
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high = 0,len(nums)-1
        while low <= high:
            mid = (low + high)/2
            if nums[high] >= nums[mid]: # #min位于左侧上升沿 等于说明有次值得情况
                high = mid
            else: #min位于左侧上升沿与右侧上升沿之间
                low = mid + 1
        return nums[low]





