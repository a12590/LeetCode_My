#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
一句话
"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        # version1 这里的reversed得到是一个object对象，需要list
        # sorted(nums, reverse=True)跟下面的区别开来。
        # 这里返回list值，它本身就是list：sorted(nums, reverse=True)[k-1]得到第k个值
        # return ' '.join(list(reversed(s.split())))

        # version2
        words = s.split()
        # 这里注意.reverse()之后不返回值
        words.reverse()
        return " ".join(words)