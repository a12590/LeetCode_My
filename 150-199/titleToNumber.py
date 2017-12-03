#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
convertToTitle
chr(x )                 将一个整数转换为一个字符
ord(x )                 将一个字符转换为它的整数值
hex(x )                 将一个整数转换为一个十六进制字符串
oct(x )                 将一个整数转换为一个八进制字符串

本质：进制转化
"""

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        ans = 0
        for e in s:
            c_n = ord(e) - ord('A') + 1
            ans = ans * 26 + c_n
        return ans
