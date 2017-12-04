#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
一趟遍历，当当前的标记last大于下一个值，那么cnt复置，重新开始
当然此前保留的ans任然在
"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = cnt = 0
        last = None
        for n in nums:
            if n > last:
                cnt +=1
                ans = max(ans,cnt)
                last = n
            else:
                last = n
                cnt =1
        return ans


if __name__ == '__main__' :
    solution = Solution()
    print solution.findLengthOfLCIS([2,2,2,2,2])