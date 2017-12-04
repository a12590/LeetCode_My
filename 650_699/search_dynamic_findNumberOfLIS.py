#!/usr/bin/python
# _*_ coding: utf-8 _*_

########################################
## 动态规划（Dynamic Programming）
## 数组dp[x]表示以x结尾的子序列中最长子序列的长度
## 数组dz[x]表示以x结尾的子序列中最长子序列的个数
########################################

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = [1] * size
        dz = [1] * size
        # 目的是通过y来跟新x的长度和个数，使用动态规划的思想
        for x in range(size):
            # 0 < y < x
            for y in range(0,x):
                # 递增,这里不处理非递增的前后两者
                if nums[y] < nums[x]:
                    # 按照递增的顺序更新
                    if dp[y] + 1> dp[x]:
                        dp[x] = dp[y]+1
                        dz[x] = dz[y]
                    # 说明在你之前有一长度等于 在你之前的长度 + 你本身，那么 += 成立
                    elif dp[y] + 1 == dp[x]:
                        dz[x] += dz[y]
        # 这里的+ [0]？!
        maxLIS = max(dp + [0])
        ans = 0
        print dp,dz
        # 一一对应关系
        for p,z in zip(dp,dz):
            if p == maxLIS:
                ans += z
        return ans

if __name__ == '__main__' :
    solution = Solution()
    print solution.findNumberOfLIS([1,3,5,4,7])
