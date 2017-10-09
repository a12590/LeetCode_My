#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
双指针（Two Pointers）
lo, hi分别指向s的左右两侧，向中心移动
当s[lo] != s[hi]时，判断删掉lo或者hi时，剩余字符串是否为回文
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda s : s == s[::-1]
        size = len(s)
        lo,hi = 0,size-1
        strPart = lambda s,x : s[:x] + s[x+1:]
        while lo < hi :
            if s[lo] != s[hi]:
                return isPalindrome(strPart(s,lo)) or isPalindrome(strPart(s,hi))
            lo +=1
            hi -=1
        return True

if __name__ == '__main__':
    a = "aba"
    b = "abca"
    solution = Solution()
    print solution.validPalindrome(a)
    print solution.validPalindrome(b)

