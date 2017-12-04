#!/usr/bin/python
# _*_ coding: utf-8 _*_

""""
stack
"""
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # 惊讶的是stack直接可以这么申明，并使用pop等函数
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1]*2)
            elif op == '+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)

if __name__ == '__main__' :
    solution = Solution()
    print solution.calPoints(["5","-2","4","C","D","9","+","+"])