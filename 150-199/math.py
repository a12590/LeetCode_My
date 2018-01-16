#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

"""

class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        negativeFlag = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        numList = []
        cnt = 0
        loopDict = dict()
        loopStr = None
        while True:
            numList.append()