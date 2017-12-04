#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
while n:
n >>1 (n/2)
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans
