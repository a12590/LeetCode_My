#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
int()
0相等
如果
"""

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        v1Arr = version1.split(".")
        v2Arr = version2.split(".")
        len1 = len(v1Arr)
        len2 = len(v2Arr)
        lenMax = max(len1,len2)
        for x in range(lenMax):
            v1Token = 0
            if x < len1:
                v1Token = int(v1Arr[x])
            v2Token = 0
            if x < len2:
                v2Token = int(v2Arr[x])
            if v1Token < v2Token:
                return -1
            if v1Token > v2Token:
                return 1
        return 0

"""
# 很精彩！！
public class Solution {
    /**
     * @param A : A string includes Upper Case letters
     * @param B : A string includes Upper Case letter
     * @return :  if string A contains all of the characters in B return true else return false
     */
    public boolean compareStrings(String A, String B) {
        if (A == null || B == null || A.length() < B.length()){
            return false;
        }
        int[] countA = new int[26];
        int[] countB = new int[26];
        for (int i = 0; i < A.length(); i++){
            countA[A.charAt(i) - 'A']++;
        }
        for (int i = 0; i < B.length(); i++){
            countB[B.charAt(i) - 'A']++;
            if (countB[B.charAt(i) - 'A'] > countA[B.charAt(i) - 'A']){
                return false;
            }
        }
        return true;
    }
}

"""
