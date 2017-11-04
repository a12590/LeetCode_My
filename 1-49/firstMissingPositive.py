#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
尽可能地把数组中不大于n（n为数组长度）的正整数放置到下标+1与其数值相同的位置上
第一个下标+1与数值不同的数字，即为所求。
例如数组nums = [3,4,-1,1]，调整位置后的结果为：[1,-1,3,4]
除第二个数字外，其余数字均满足nums[i] = i + 1，因此返回2
"""

"""
桶排序的思想
每当A[i]!= i+1 的时候，将A[i] 与A[A[i]-1] 交换，直到无法
交换为止，终止条件是A[i]== A[A[i]-1]。
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] < n \




if __name__ == '__main__':
    nums = [1,2,0]
    nums2 = [3,4,-1,0]
    solution = Solution()
    print solution.firstMissingPositive(nums)