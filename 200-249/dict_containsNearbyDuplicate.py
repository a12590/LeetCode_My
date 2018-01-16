#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
python
dict(value:idx)
.haskey
.get
dict[num[i]] = i
abs()

java
//HashTable<value,list of duplicates>\HashMap<>()
for (int i = 0; i < nums.length; i++ )

map(Integer,List<Integer>)
.containsKey
.get

map 两种添加方式：get add
map.get(num[i]).add(i) 或者 map.put(num[i],i)

Math.abs()


"""

##############
## HashSet<>() Set<Integer>
## remove add
##
##############


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        numDict = dict()
        for x in range(len(nums)):
            # 不需要像java 一般判断是否存在,有可能返回多个吗
            # TODO
            idx = numDict.get(nums[x])
            # 这里 x > idx：x 递增
            if idx >= 0 and x - idx <= k:
                return True
            numDict[nums[x]] = x


"""
class Solution{
    public boolean containsNearbyDuplicate(int[] nums,int k){
        if (nums == null || nums.length == 0 || k <= 0){
            return false;
        }
        final Map<Integer,List<Integer>> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if (map.containsKey(nums[i])){
                for(int index : map.get(nums[i])){
                    if (Math.abs(index - i) <= k){
                        return true;
                    }
                }
            } else{
                map.put(nums[i],new ArrayList<>());
            }
            map.get(nums[i]).add(i);
        }
        # ...
        return false;
    }
}
"""