#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

"""

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # stack 入栈，minStack 判断最值
        self.stack.append(x)
        # 极限情况：第一次入最小值栈，此外还要考虑多个最小值情况
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        # minStack的出栈，某些情况出栈
        #这个不行，把自己绕晕了：self.minStack[-1] == self.getMin():
        # if len(self.minStack) and self.minStack[-1] == self.getMin():
        if self.top() == self.getMin():
            self.minStack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minStack):
            return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()