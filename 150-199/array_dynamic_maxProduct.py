#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
动态规划：核心是存储+更新
这里更机智：不再考虑正负，就比较可能的最值。如果是负号的最大（小）值和如果是正号的最大（小）值
prevMax = fmax;
fmax = Math.max(Math.max(nums[i] * prevMax, nums[i]), nums[i] * fmin);
fmin = Math.min(Math.min(nums[i] * prevMax, nums[i]), nums[i] * fmin);
# 就一句行的
ans = Math.max(ans, fmax);
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = max(nums)
        size = len(nums)
        # 这两个是list类型
        positive_max = [0 for x in range(size)]
        negative_min = [0 for x in range(size)]
        if nums[0] > 0:
            positive_max[0] = nums[0]
        else:
            negative_min[0] = nums[0]
        for x in range(1,size):
            if nums[x] > 0:
                positive_max[x] = max(nums[x],positive_max[x-1] * nums[x])
                # 连续 ，不是当前数，就是连续乘积
                negative_min[x] = negative_min[x-1] * nums[x]
            elif nums[x] < 0:
                positive_max[x] = negative_min[x-1] * nums[x]
                negative_min[x] = min(nums[x],positive_max[x-1] * nums[x])
            # 求ans 更新条件
            if positive_max[x] and positive_max[x] > ans:
                ans = positive_max[x]
        return ans

"""
public class Solution {
    public int maxProduct(int[] nums) {
        # int[].length str.length()
        if (nums == null || nums.length == 0){
            return 0;
        }
        int[] max = new int[nums.length];
        int[] min = new int[nums.length];
        # 第一个也行
        int rst = max[0];
        for(int i = 1; i < nums.length; i++){
            if (nums[i] > 0){
                max[i] = Math.max(nums[i],max[i - 1] * nums[i]);
                min[i] = Math.max(nums[i],max[i - 1] * nums[i]);
            }else {
    			max[i] = Math.max(nums[i], min[i - 1] * nums[i]);
    			min[i] = Math.min(nums[i], max[i - 1] * nums[i]);
    		}
    		rst = Math.max(rst, max[i]);
        }
        return rst;
    }
}
"""

"""

public class Solution {
    /**
     * @param nums: an array of integers
     * @return: an integer
     */
    public int maxProduct(int[] nums) {

    }
}
"""
