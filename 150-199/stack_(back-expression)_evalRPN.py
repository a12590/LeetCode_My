#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
对字符串的处理，Python: int()，C++/C: atoi()，Java: Integer.parseInt()。
需要注意的是 Python 的 / 操作。
例如，在Java中，6 / (-132) == 0（Java使用的是截断），
而在Python中，6 / (-132) == -1（Python使用的是floor）。
因此对除法的处理可以采用：int(float(x) / y)，即可与Java的结果保持一致。
"""

class Solution:
	# @param tokens, a list of string
	# @return an integer
    def evalRPN(self, tokens):
        stack = []
        for str in tokens:
            if str not in '+-*/':
                tmp = int(str)
                stack.append(tmp)
            else:
                a = stack.pop()
                b = stack.pop()
                if str == '+': stack.append(b + a)
                if str == '-': stack.append(b - a)
                elif str == '*':
                    stack.append(b * a)
                elif str == '/':
                    stack.append(int(b * 1.0 / a))
        return stack[0]

    #     operators = ["+", "-", "*", "/"]
    #     operand_list = []
    #     for token in tokens:
    #         if token in operators:
    #             y,x = operand_list.pop(),operand_list.pop()
    #             operand_list.append(self.getVal(x,y,token))
    #         else:
    #             operand_list.append(int(token))
    #     return operand_list[0]
    #
    # # 不会这种封装没事。看版本2
    # def getVal(self,x,y,operator):
    #     return {
    #         '+': lambda x,y:x+y,
    #         '-': lambda x,y:x-y,
    #         '*': lambda x,y:x*y,
    #         '/': lambda x,y:int(float(x)/y)
    #         }[operator](x,y)





