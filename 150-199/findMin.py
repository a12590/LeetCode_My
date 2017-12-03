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
        # 这里 low、high最后会是同一个
        # 如果采取nums[mid] > nums[mid + 1]的判断方式则low 不可能等于high
        while low <= high:
            mid = (low + high)/2
            # 这里也没错
            # (nums[mid] > nums[mid + 1])这样判断的话，需要考虑有序情况。
            # 而且，就是那个mid。
            # 这里需要考虑mid 与mid +1或者mid-1 与mid
            if nums[high] >= nums[mid]: # #min位于左侧上升沿
                high = mid
            else: #min位于左侧上升沿与右侧上升沿之间
                low = mid + 1
        return nums[low]





