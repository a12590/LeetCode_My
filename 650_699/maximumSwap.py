#!/usr/bin/python
# _*_ coding: utf-8 _*_

""""
记输入整数为num，其每位数字的数组为nums，倒序排列后的数组为numt
从左向右（高位到低位）遍历nums, numt，记当前数字分别为m, n, 下标为i
若m != n：则将nums[i + 1 .. size]的最后一个最大值maxv与m对调
将nums恢复为数字并返回
"""

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """