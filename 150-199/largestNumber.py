#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
cmp=self.compare
[1,-1][a + b > b + a] 升序规则
lstrip rstrip strip：可以去除多个

"""

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted([str(x) for x in num] ,cmp=self.compare)
        print num
        ans = ''.join(num).lstrip('0')
        return ans

    def compare(self,a,b):
        return [1,-1][a + b > b + a]


if __name__ == '__main__':
    num = [3, 30, 34, 5, 9]
    solution = Solution()
    print solution.largestNumber(num)


