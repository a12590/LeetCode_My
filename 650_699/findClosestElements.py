#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

"""
import bisect

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if k ==0 or arr == None:
            return
        ans = []
        index = bisect.bisect_left(arr, x)
        lo = hi = index
        print index
        ans.append(arr[index])
        k -=1
        while(k):
            if (x - arr[lo - 1]) > (arr[hi + 1] -x) and lo >=1 and hi <len(arr)-1:
                print "dsd"
                hi +=1
                ans.append(arr[hi])
                k -= 1
            elif (x - arr[lo - 1]) <= (arr[hi + 1] -x) and lo >=1 and hi <len(arr)-1:
                print "sd"
                lo -=1
                ans.append(arr[lo])
                k -= 1
        return sorted(ans)

if __name__ == '__main__' :
    solution = Solution()
    print solution.findClosestElements([1,2,3,4,5], k=4, x=-1)