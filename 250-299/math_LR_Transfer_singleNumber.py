#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
两数据不同，至少有一个位不同
A ^  N1 ^ N2 ^ ... B
从位的角度看：
把 0-32 每位，所有数中对应的位做统计？

还是先找出至少有一个位不同的一位即可，然后在该位上分别做 异或操作

"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        pass

"""
public class Solution {
    /**
     * @param A : An integer array
     * @return : Two integers
     */
    // int 类型 16,32（大多数）
    public List<Integer> singleNumberIII(int[] A) {
        if (A == null || A.length == 0){
            return null;
        }
        int num = 0
        for (int i = 0; i < A.length; i++){
            num ^= A[i];
        }
        for (int i = 0;i< 32;i++){
            int a = 0;
            a = num >> i & 1;
            if (a != 0) a = i;
        }
        rstA = 0;
        rstB = 0;
        for (int i = 0; i < A.length; i++){
            bit = A[i] >> a & 1;
            if (bit) rstA = rstA ^ A[i];
            rstB = rstB ^ A[i];
        }
        List<Integer> rst = new ArrayList<Integer>();
        rst.add(rstA);
        rst.add(rstB);
        return rst;
    }
}
"""