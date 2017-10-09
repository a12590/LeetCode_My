#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
创建字典dmap<String, Set>
build操作：用下划线'_'替换word的每一个位置的字母，作为Key，被替换的字母作为Value，存入dmap
search操作：用下划线'_'替换word的每一个位置的字母，作为Key，在dmap中查找与被替换字母不同的值

此题注意点：
1、需要有不同。不是长度上，而是单个字符；保存原来的单个字符，比对
"""
import collections


class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dmap = collections.defaultdict(set)

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            # range 的使用
            for x in range(len(word)):
                key = word[:x] + '_' + word[x+1:]
                self.dmap[key].add(word[x])

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for x in range(len(word)):
            key = word[:x] + '_' + word[x+1:]
            values = self.dmap[key]
            # 找不到继续
            if not values :continue
            # 找到,两值不同
            # values : str not in set ,这里加深我对self.dmap = collections.defaultdict(set)的认识
            # or len(values) > 1 这个是指 ["hello","hallo"] 查 hello时此时 满足e in values ，可是values中长度大于1
            if word[x] not in values or len(values) > 1:
                return True

        return False

if __name__ == '__main__':
    obj = MagicDictionary()
    dict = ["hello", "hallo","leetcode"]
    obj.buildDict(dict)
    word = "hello"
    param_2 = obj.search(word)
    print param_2