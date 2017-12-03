#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
从一个未经排序的数组中找出第k大的元素。

陷阱：注意是排序之后的第k大，而非第k个不重复的元素
"""
import random


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        # 不是首尾？
        pivot = random.choice(nums)
        # 不是移动？
        nums1,nums2 = [],[]
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1,k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2,k - (len(nums) -len(nums2)))
        return pivot

