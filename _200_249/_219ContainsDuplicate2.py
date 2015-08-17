'''  
@author: yang
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        index = 0
        for item in nums:
            dic[index] = item
            index += 1
        l = sorted(dic.items(), key=lambda d:d[1])
        index = 0
        for item in l[:-1]: 
            if(item[1]==l[index+1][1] and abs(item[0]-l[index+1][0])<=k):
                return True
            index += 1
        return False
    
testNums = [1,2,3,4,5,8,9,7]

result = Solution().containsNearbyDuplicate(testNums, 3)
print(result)
