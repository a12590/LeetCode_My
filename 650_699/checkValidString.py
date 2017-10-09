#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
遍历s中的字符c，利用集合vset记录所有当前左括号-右括号的差值
  若c == '('，将vset替换为其所有元素+1
  若c == ')'，将vset替换为其所有不小于1的元素 - 1
  若c == '*’，将vset中的所有元素+1，-1后，保留非负元素
遍历结束，判断vset中是否包含0元素
当前二字，由于* 两种情况，增加了各种数值，只要满足一种情况为0即可
"""

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vset = set([0])
        for c in s:
            nset = set()
            if c == '(':
                for v in vset:
                    nset.add(v+1)
            elif c == ')':
                for v in vset:
                    if v >= 1:
                        nset.add(v-1)
            elif c == '*':
                for v in vset:
                    # 增加一当前左括号-右括号的差值+1的元素
                    nset.add(v+1)
                    nset.add(v)
                    if v >= 1:
                        nset.add(v - 1)
            vset = nset
            print vset
        return 0 in vset

if __name__ == '__main__' :
    solution = Solution()
    print solution.checkValidString("(*)")