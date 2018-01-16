#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
bin(x ^ y )
Count('1')
"""

"""
忘了的话。使用XOR (^) 以及 遍历右移 >>1，& + 求与累加
"""

class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x ^ y).count('1')

"""
class Solution {
    public int hammingDistance(int x, int y) {
        int xor = x ^ y;
        int count = 0;
        while(xor != 0){
            count += xor & 1;
            xor = xor >> 1;
        }
        return count;
    }
}
"""