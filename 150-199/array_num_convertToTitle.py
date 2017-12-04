#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
chr(x )                 将一个整数转换为一个字符
ord(x )                 将一个字符转换为它的整数值
hex(x )                 将一个整数转换为一个十六进制字符串
oct(x )                 将一个整数转换为一个八进制字符串

"""

class Solution:
    # @return a string
    def convertToTitle(self, num):
        ans = ""
        while num:
            ans = chr((num - 1) % 26 + ord('A')) + ans
            num = (num - 1)/26
        return ans