'''  

@author: yang
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        limit = len(nums)//2
        dic = {}
        for item in nums:
            try:
                dic[item] += 1
            except:
                dic[item] = 1
            if(dic[item]>limit):
                return item
        