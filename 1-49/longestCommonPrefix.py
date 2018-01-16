#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

"""

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ''
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or str[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]