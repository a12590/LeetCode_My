#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

"""

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if not len(num):
            return 0
        ret = num[0] + num[1] + num[2]
        num.sort()
        # k len(num)-1 i -3 j -2
        for i in range(len(num)-2):
            j = i + 1
            k = len(num)-1
            # 这里i 不变 j、k变化
            while j < k:
                tsum = num[i] + num[j] + num[k]
                if abs(tsum - target) < abs(ret - target):
                    ret = tsum
                if tsum < target:
                    j +=1
                if tsum > target:
                    k -=1
                else:
                    k -=1
                    j +=1
        return ret
