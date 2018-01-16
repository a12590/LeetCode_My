#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
java
TreeSet
floor <=
ceiling >=

Long target = treeSet.ceiling((long)nums[i] - t);
target <= (long)nums[i] + t

set.floor(n) != null && n <= t + set.floor(n) ||
                    set.ceiling(n) != null && set.ceiling(n) <= t + n

1. floor()方法返set中≤给定元素的最大元素；如果不存在这样的元素，则返回 null。
2. ceiling()方法返回set中≥给定元素的最小元素；如果不存在这样的元素，则返回 null。

最大的元素大于某个值，如果不存在，那就不存在
最小的元素小于某个值，如果不存在，那就不存在

int[] nums int k int t
if(k< 1 || t < 0)
    return false;
TreeSet<Integer> set = new TreeSet<Integer>();
for(int i = 0; i < nums.length; i++ ){
    int n = nums[i];
    if (set.floor(n) != null && n <= t + set.floor(n) ||
        set.ceiling(n) != null && set.ceiling(n) <= t + n)
        return true
    #     跟新set
    set.add(n);
    # 当元素达到k范围外的时候，移除元素，下标i-k
    if (i >= k)
        set.remove(nums[i - k);
}
return false;


"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):


