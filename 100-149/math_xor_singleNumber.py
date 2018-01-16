#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans

"""
class Solution {
    public int singleNumber(int[] nums) {
        if (nums.length == 0 || nums == null){
            return 0;
        }
        # 0 , 1
        for (int i = 1; i < nums.length; i ++){
            nums[0] = nums[0] ^ nums[i]
        }
        return nums[0];
    }
}
"""