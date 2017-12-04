#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
基本功：double、正负0数
二分法(递归)：xn = xn/2 * xn/2 * xn%2
需要考虑 n偶奇
if n偶：xn = xn/2 * xn/2
else：xn = xn/2 * xn/2 * x
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0 :
            n = -n
            x = 1/x
        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x * x, n / 2)

