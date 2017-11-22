#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
这里的
dp[0]额外推出为1
dp[1] = [1 + dp[0]] = dp[0]
dp[2] = [1+dp[1]] +[2+dp[0]]  = dp[1] + dp[0]
dp[3]= [1+dp[2]] +  [2+dp[1]] = dp[2] + dp[1]
dp[4] = [1+dp[3]] + [2+dp[2]] = dp[3] + dp[2]
...
循环赋值
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for x in range(2,n+1):
            dp[x] = dp[x-1] + dp[x-2]
        return dp[x]


