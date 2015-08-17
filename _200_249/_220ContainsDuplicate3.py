''' 

@author: yang
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        dic = {}
        index = 0
        for item in nums:
            dic[index] = item
            index += 1
        l = sorted(dic.items(), key=lambda d:d[1])
        index = 0
        for item in l[:-1]: 
            j = 1
            while(index+j<len(l) and abs(item[1]-l[index+j][1])<=t):
                if(abs(item[0]-l[index+j][0])<=k):
                    return True
                else:
                    j += 1
            index += 1
        return False
    
testNums = [1,3,6,2]

result = Solution().containsNearbyAlmostDuplicate(testNums, 1,2)
print(result)
