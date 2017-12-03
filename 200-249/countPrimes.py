#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
?
"""
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        isPrime = [True] * max(n,2)
        isPrime[0],isPrime[1] = False,False
        # 0,1 不是质数
        x = 2
        # 小于根号n
        while x * x < n:
            if isPrime[x]:
                # ?
                p = x * x
                while p < n:
                    isPrime[p] = False
                    p += x
            x += 1
        # ?
        return sum(isPrime)

