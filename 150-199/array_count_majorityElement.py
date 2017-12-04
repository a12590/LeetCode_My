#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
“投票算法”
当前可能的候选众数\该候选众数的出现次数
遍历数组num,计数.这个跟操作系统一东西的很像
if count == 0:
    major = i;
count += (major == i) ? 1:-1;
"""

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        candidate,count = None,0
        for e in num:
            if count == 0:
                candidate,count = e,1
            elif e == candidate:
                count += 1
            else:
                count -= 1
        return candidate
