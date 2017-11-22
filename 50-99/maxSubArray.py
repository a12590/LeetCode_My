#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
设状态为f[j]，表示以S[j] 结尾的最大连续子序列和

设状态为f[j]，表示以S[j] 结尾的最大连续子序列和，则状态转移方程如下：
f[j] = max{f[j-1] + S[j],S[j]}; 其中 0<j<n+1
target = max{f[j]}; 其中 0<j<n+1
"""

"""
我的版本：
if not nums:
    return 0
sum = nums[0]
size = len(nums)
for x in range(0,size):
    sum = max(num[x],sum + nums[x])
    if sum < 0 :
        sum = nums[x]
return sum

一旦sum变为负数。sum从当前数计算。这是不对，那以前的大数就不管了？
所以要有maxSum保存以前的最大值，curSum动态变化
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curSum = maxSum = nums[0]
        #
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    solution = Solution()
    print solution.maxSubArray(nums)

