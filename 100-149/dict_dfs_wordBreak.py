#!/usr/bin/python
# _*_ coding: utf-8 _*_

# TODO：没搞懂
"""
记忆化搜索

在搜索过程中，
使用字典tokenDict将已经搜索过的子句的拆解方案记录下来，从而实现DFS的剪枝
"""
import collections

# class Solution(object):
#     def wordBreak(self, s, wordDict):
#         """
#         :type s: str
#         :type wordDict: List[str]
#         :rtype: List[str]
#         """
#         tokenDict = collections.defaultdict()
#         def dfs(s):
#             ans = []
#             # 出口
#             if s in wordDict:
#                 ans.append(s)
#             for x in range(len(s)):
#                 prefix, suffix = s[:x], s[x:]
#                 if prefix not in wordDict:
#                     continue
#                 rest = []
#                 # 这里的 rest 需要通过递归得到，增加了记忆功能，不用每次都遍历一遍。
#                 if suffix in tokenDict:
#                     rest = tokenDict[suffix]
#                 else:
#                     rest = dfs(suffix)
#                 for n in rest:
#                     ans.append(prefix + ' ' + n)
#             # 全局变量，每次都可以使用。相当于记忆
#             tokenDict[s] = ans
#             return ans
#
#         return dfs(s)

# 不要这个记忆功能也能实现

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        tokenDict = collections.defaultdict()
        def dfs(s):
            ans = []
            # 出口
            if s in wordDict:
                ans.append(s)
            for x in range(len(s)):
                prefix, suffix = s[:x], s[x:]
                if prefix not in wordDict:
                    continue
                rest = dfs(suffix)
                # 这里的 rest 需要通过递归得到，增加了记忆功能，不用每次都遍历一遍。
                # if suffix in tokenDict:
                #     rest = tokenDict[suffix]
                # else:
                for n in rest:
                    ans.append(prefix + ' ' + n)
            # 全局变量，每次都可以使用。相当于记忆
            # tokenDict[s] = ans
            return ans

        return dfs(s)

if __name__ == '__main__':
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    solution = Solution()
    print solution.wordBreak(s,dict)

"""
public class Solution {
    public boolean wordBreak(String s, Set<String> dict) {
    if (s == null || dict.contains(s)){
        return true;
    }
    boolean[] valid = new boolean[s.length() + 1];
    valid[s.length()] = true;
    int maxLength = calMaxLength(dict);
    for(int i = s.length()-1;i>=0;i--){
        for(int j=i;j<s.length() && (i-j) <= maxLength;j++){
            if (valid[j+1] && dict.contains(s.substring(i,j+1))){
                valid[i] = true;
                break;
            }
        }
    }
    return valid[0];
}

    public int calMaxLength(Set<String> dict){
        int length = 0;
        for(String word:dict){
            length = Math.max(length,word.length());
        }
        return length;
    }

}
"""