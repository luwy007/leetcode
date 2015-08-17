''' 

@author: Administrator
'''
from numpy.core.multiarray import ITEM_HASOBJECT
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        output = [1]*len(nums)
        
        temp = 1
        for index,item in enumerate(nums[:-1]):
            temp *= item
            output[index+1] = temp
            
        temp = 1
        for index in range(len(nums)-1):
            temp *= nums[-index-1]
            output[-index-2] *= temp
        return output
            
if __name__=="__main__":
    nums = [1,2,3,4,5]
    for item in nums[:-1]:
        print(item)
    res = Solution().productExceptSelf(nums)
    print(res)
                