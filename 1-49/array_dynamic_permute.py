#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
递归（Recursion）
记传入数组为nums，若nums的长度不大于1，则直接返回[nums]
遍历nums，从中抽取一个数num，递归计算剩余数字组成的数组n，然后将num与结果合并
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <=1 :return [nums]
        ans = []
        # 还是没深度地体会 num 和 i 在此场景中的意义
        for i,num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for y in self.permute(n):
                ans.append([num] + y)
        return ans

if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    print solution.permute(nums)