#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
从一个未经排序的数组中找出第k大的元素。
陷阱：注意是排序之后的第k大，而非第k个不重复的元素
"""
import random

# class Solution:
#     # @param {integer[]} nums
#     # @param {integer} k
#     # @return {integer}
#     def findKthLargest(self, nums, k):
        # # 递归，还是用回下面的
        # pivot = random.choice(nums)
        # # 以空间
        # nums1,nums2 = [],[]
        # for num in nums:
        #     if num < pivot:
        #         nums1.append(num)
        #     elif num > pivot:
        #         nums2.append(num)
        # if k <= len(nums1):
        #     return self.findKthLargest(nums1,k)
        # if k > len(nums) - len(nums2):
        #     return self.findKthLargest(nums2,k - (len(nums) -len(nums2)))
        # return pivot

# 时间复杂度：O(n)

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        left,right = 0, len(nums) - 1
        while (1):
            pos = self.partion(nums,left,right)
            if pos == k -1:
                return nums[pos]
            if pos > k -1:
                right = pos -1
            else:
                left = pos + 1

    def partion(self, nums, left, right):
        # 保存变量left处值
        pivot = nums[left]
        l ,r = left + 1, right
        while (l <= r):
            while (l <= r and nums[l] <= pivot):
                l += 1
            while (l <= r and nums[r] >= pivot):
                r -= 1
            if (l <= r):
                nums[l],nums[r] = nums[r], nums[l]
        # left做最后的交换
        nums[left],nums[r] = nums[r],nums[left]
        return r

        # 思考这个为什么不行？这个直接就把值陆续改了
        # pivot = nums[left]
        # # 如果没有加一，while(l<r)
        # while (left < right):
        #     while left < right and nums[left] <= pivot:
        #         left += 1
        #     while left < right and nums[right] >= pivot:
        #         right -= 1
        #     nums[left] = nums[right]
        # print nums
        # nums[right] = pivot
        # print right
        # return right

if __name__ == '__main__':
    solution = Solution()
    nums = [4,5,7,9,2,5,1]
    # print solution.partion(nums,0,6)
    print solution.findKthLargest(nums,6)