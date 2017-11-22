#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
dp[x][y] = dp[x-1][y] + dp[x][y-1]
"""
import operator

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp = [[0] * n for i in range(m)]
        # dp[0][0] = 1
        # for x in range(m):
        #     for y in range(n):
        #         if x + 1 < m:
        #             dp[x+1][y] += dp[x][y]
        #         if y + 1 < n:
        #             dp[x][y+1] += dp[x][y]
        # return dp[x][y]
        if m < n:
            m,n = n,m
        # 这里要range(x,y) 左闭右开
        mul = lambda x,y : reduce(operator.mul,range(x,y),1)
        # 推导公式
        return mul(m,m+n-1)/mul(1,n)

if __name__ == '__main__':
    solution = Solution()
    print solution.uniquePaths(1,10)