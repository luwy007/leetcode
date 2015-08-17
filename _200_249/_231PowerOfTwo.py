'''  

@author: yang
'''
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if(n<=0):
            return False
        if(n<1):
            n = 1/n
        if(n%1!=0):
            return False
        x = bin(n)[3:]
        sum = 0
        for i in x:
            if('1'==i):
                return False
        return True

obj = Solution()
print(obj.isPowerOfTwo(3))