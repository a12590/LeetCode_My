#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

"""
import collections

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        # cache OrderedDict 近期最少使用的元素。
        self.cache = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.cache:
            return -1
        value = self.cache.pop(key)
        # 被访问，cache{key:value}
        self.cache[key] = value
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            # popitem
            self.cache.popitem(last=False)
        self.cache[key] = value




        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)