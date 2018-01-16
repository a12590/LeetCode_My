#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
我困惑的地方在于二分法查找，条件的不互斥吧？
这个java好理解点，递归会比较难懂
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        size = len(num)
        return self.search(num,0,size - 1)

    def search(self,num,start,end):
        if start == end:
            return start
        if start + 1 == end:
            # 注意判断条件满足下：返回end
            return [start,end][num[start] < num[end]]
        mid = (start + end)/2
        if num[mid] < num[mid -1]:
            #
            return self.search(num,start,mid-1)
        if num[mid] < num[mid + 1]:
            return self.search(num,mid + 1,end)
        # num[mid + 1] <= num[mid] >= num[mid -1]
        return mid

"""
class Solution{
    public int findPeak(){
        int start = 1;
        int end = A.length - 2;
        int mid;
        while(start + 1 < end){
            mid = start + (start - end )/2;
            if (A[mid] > A[mid -1] && A[mid] > A[mid + 1]){
                return mid;

            # TODO
            }else if (A[mid] > A[start] && A[mid] < A[mid + 1]){
                start = mid;
            } else {
                end = mid;
            }
        }
    }
}

"""