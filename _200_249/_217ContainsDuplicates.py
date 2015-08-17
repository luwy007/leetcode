'''  
@author: yang
'''
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        dic = {}
        for item in nums:
            if(dic.__contains__(item)):
                return False
            else:
                dic[item] = 1
        return True