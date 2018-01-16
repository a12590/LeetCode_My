#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
 public static int find(String str){
        if(str==null||str.length()==0){
            return -1;
        }
        int len = str.length();
        char[] letter = str.toCharArray();
        int[] count = new int[26];
        for (int i = 0; i < len ; i++){
            char curChar = letter[i];
            count[curChar - 'a']++;
        }
        for (int i = 0; i<len;i++){
            char curChar = letter[i];
            if (count[curChar - 'a'] == 1){
                return i;
            }
        }
        return -1;
}
"""