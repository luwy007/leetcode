'''  

@author: yang
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k): 
        temp = []
        for item in nums[:k]:
            temp.append(item)
        temp.sort(reverse = True)
        for item in nums[k:]:
            if(item>temp[-1]):
                self.insert(temp, item)
        return temp[-1] 
    
    def insert(self,temp,item):
        if(len(temp)==1):
            temp[0] = item
            return
        for index in range(2,len(temp)+1):
            if(temp[-index]<item):
                temp[-index+1] = temp[-index]
            else:
                temp[-index+1] = item
                return
        temp[0] = item
        return
    
if __name__=="__main__":
    nums = [3,2,3,1,2,4,5,5,6] 
    print(Solution().findKthLargest(nums, 4))