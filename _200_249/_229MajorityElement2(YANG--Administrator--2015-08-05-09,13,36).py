'''  
@author: yang
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        
        a, b, ca, cb = 0, 1, 0, 0
        for num in nums:
            if a == num:
                ca += 1
            elif b == num:
                cb += 1
            elif ca == 0:
                a, ca = num, 1
            elif cb == 0:
                b, cb = num, 1
            else:
                ca -= 1
                cb -= 1
        ca = len([0 for num in nums if num == a])
        cb = len([0 for num in nums if num == b])
        res = []
        if ca > len(nums) / 3:
            res.append(a)
        if cb > len(nums) / 3:
            res.append(b)
        return res
        
        
        limit = len(nums)//3
        dic = {}
        temp = {}
        for item in nums:
            try:
                dic[item] += 1
            except:
                dic[item] = 1
            if(dic[item]>limit): 
                temp[item] = 1
                if(len(temp)>1):
                    break
        result = []
        for item in temp:
            result.append(item)
        return result
    
    
    
    
    
    
    
    
    
    
    
if __name__=="__main__":
    res = Solution().majorityElement([2,3,1,2,3,4,4,4,4,3,3])
    print(res)
    
    
    
    
    
    
    
    
    
    