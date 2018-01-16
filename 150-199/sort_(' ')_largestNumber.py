#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
cmp=self.compare
[1,-1][a + b > b + a] 升序规则
lstrip rstrip strip：可以去除多个

"""

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        # python 记住sorted cmp即可
        num = sorted([str(x) for x in num] ,cmp=self.compare)
        print num
        # 0
        ans = ''.join(num).lstrip('0')
        return ans

    def compare(self,a,b):
        # 残念告诉我 true -1
        return [1,-1][a + b > b + a]


if __name__ == '__main__':
    num = [3, 30, 34, 5, 9]
    solution = Solution()
    print solution.largestNumber(num)


"""
class CustomComparator implements  Comparator<String> {
    public int compare(String s1, String s2) {
        # 顺序？
        return (s2 + s1).compareTo(s1 + s2);
    }
}

public class Solution{
    public String largestNumber(int[] num){
        if (num == null || num.length == 0){
            return "";
        }
        String[] strs = new String[num.length];
        for (int i = 0;i < num.length; i++){
            strs[i] = num[i] + "";
        }
        # Array.sort new CustomComparator()
        Arrays.sort(strs,new CustomComparator());
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < num.length; i++) {
            sb.append(strs[i]);
        }
        String rst = sb.toString();
        # 0
        if (rst.charAt(0) == '0'){
            return "0";
        }
        return rst;
    }
}
"""

