#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

"""

class Solution:
    # @param {string} s
    # @return {integer}
    # 后缀表达式求值
    def calculate(self, s):
        tokens = self.toRPN(s)
        return self.evalRPN(tokens)

    operators = ['+','-','*','/']
    # 中缀表达式转为后缀表达式
    def toRPN(self,s):
        tokens,stack = [],[]
        number = ''
        for c in s:
            if c.isdigit():
                # 数字时，加入后缀表达式；
                number += c
                # 运算符：
            else:
                if number:
                    tokens.append(number)
                    number = ''
                # c.若为除括号外的其他运算符， 当其优先级高于除 '('以外的栈顶运算符时，直接入栈。
                # 否则从栈顶开始，依次弹出比当前处理的运算符优先级高和优先级相等的运算符，
                # 直到一个比它优先级低的或者遇到了一个左括号为止。
                if c in self.operators:
                    while len(stack) and self.getPriority(
                        stack[-1] >= self.getPriority(c)):
                        tokens.append(stack.pop())
                # a. 若为 '('，入栈；
                elif c == '(':
                    stack.append(c)
                # b. 若为 ')'，则依次把栈中的的运算符加入后缀表达式中，直到出现'('，从栈中删除'(' ；
                elif c == ')':
                    while len(stack) and stack[-1] != '(':
                        tokens.append(stack.pop())
                    stack.pop()
        if number:
            tokens.append(number)
        # ·当扫描的中缀表达式结束时，栈中的的所有运算符出栈；
        while len(stack):
            tokens.append(stack.pop())
        return tokens



    def evalRPN(self, tokens):
        # 建立一个栈S
        operands = []
        for token in tokens:
            # 如果读到n元运算符(即需要参数个数为n的运算符)则取出由栈顶向下的n项按操作符运算，
            # 再将运算的结果代替原栈顶的n项，压入栈S中
            if token in self.operators:
                y, x = operands.pop(), operands.pop()
                operands.append(self.getVal(x, y, token))
            # 从左到右读表达式，如果读到操作数就将它压入栈S中
            else:
                operands.append(int(token))
        return operands[0]

    def getVal(self,x,y,operator):
        return {
            '+': lambda x ,y :x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(float(x) / y),
        }[operator](x, y)

    def getPriority(self,operator):
        return {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        }.get(operator,0)
