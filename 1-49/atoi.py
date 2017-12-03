#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
1、空白字符
2、正负号 , 还有没有正号的
3、非法字符
4、数值超出了整数范围，返回
INT_MAX (2147483647) 或者 INT_MIN (-2147483648)
"""

class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip(" ")
        # 一般这里有一个0判定
        if str == '':
            return 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        ret = 0
        pos = 0
        sign = 1
        overflow = 0

        if str[0] == '-':
            pos +=1
            sign = -1
        elif str[0] == '+':
            pos +=1
        for i in range(pos,len(str)):
            if not str[i].isdigit():
                break
            # 就一句
            ret = ret * 10 + int(str[i])
            if not INT_MIN <= ret * sign <= INT_MAX:
                overflow = 1

        if overflow:
            if ret * sign > INT_MAX:
                return  INT_MAX
            elif ret * sign < INT_MIN:
                return INT_MIN
        else:
            return ret * sign

if __name__ == '__main__':
    str = "-145ew"
    solution = Solution()
    print solution.atoi(str)

