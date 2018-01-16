#!/usr/bin/python
# _*_ coding: utf-8 _*_

class Solution(object):
    def numberToWords(self, num):
        lv1 = "One Two Three Four Five Six Seven Eight Nine Ten \
               Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        lv2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        def word(num):
            if num < 20:
                return lv1[num-1]
            if num < 100:
                return lv2[num/10 - 2] + ' ' + word(num%10)
            if num < 1000:
                return lv1[num/100-1] + " Hundred " + lv2[(num%100)/10-2] + " "+ word(num%10)
            for p,w in enumerate(("Thousand","Million","Billion"),1):
                if num < 1000**(p+1):
                    return word(num/1000**p) + ' ' + str(w)+ " "+ word(num%1000**p)
        if num == 0:
            return 'Zero'
        else:
            return word(num)

if __name__ == '__main__':
    num = 1234567891
    solution = Solution()
    print solution.numberToWords(num)

