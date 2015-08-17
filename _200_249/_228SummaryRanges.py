'''  
@author: yang
'''
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        
        result = []
        head = nums[0]
        tail = nums[0]
        lastOne = nums[0]
        for x in nums[1:]:
            if(x==lastOne+1):
                lastOne = x
                tail = x
            else:
                if(head==tail):
                    result.append("%i"%head)
                else:
                    result.append("%i->%i"%(head,tail))
                head = x
                tail = x
                lastOne = x
        if(head==tail):
            result.append("%i"%head)
        else:
            result.append("%i->%i"%(head,tail))  
        return result
        
obj = Solution()
nums = [0,1,2,4,6,7]
print(obj.summaryRanges(nums))       