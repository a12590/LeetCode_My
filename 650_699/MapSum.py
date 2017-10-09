#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
TrieNode包含属性：sum（当前节点子树的和），val（当前节点的值）
insert操作：向字典树中插入节点，并将沿途节点记录下来。更新途经节点的sum值
sum操作：直接返回前缀对应节点的sum值
"""
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = dict()
        self.sum = 0
        self.val = 0

class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """



        # Your MapSum object will be instantiated and called as such:
        # obj = MapSum()
        # obj.insert(key,val)
        # param_2 = obj.sum(prefix)