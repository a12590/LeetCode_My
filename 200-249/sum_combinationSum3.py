#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
当前统计值，总数
cnt, k
sums, n
出错结束条件：cnt,sums两个任一个超值
满足结束条件：两个都满足条件
最难这里：
一
x:1~9
start x
cnt +1
sums +x
nums +[x]
二
return？是break？不吧？
"""

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        ans = []
        def search(start,cnt,sums,nums):
            if cnt > k or sums > n:
                return
            if cnt == k and sums == n:
                # 这里
                ans.append(nums)
                return
            for x in range(start + 1,10):
                search(x,cnt+1,sums+x,nums+[x])
        search(0,0,0,[])
        return ans
