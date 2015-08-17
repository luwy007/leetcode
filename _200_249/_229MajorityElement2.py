'''  
@author: yang
'''

import string


def normalize(num, max_len):# change each number into form like +/-000123 
    s = str(num)
    sign = True
    if s[0] == '-':
        sign = False
        s = s[1:]
    return ('+' if sign else '-') + ((max_len - len(s)) * '0') + s


def index(symbol):          #ord('1')=49, ord('2')=50
    if symbol == '+':
        return 10
    if symbol == '-':
        return 11
    return ord(symbol) - ord('0')


def is_candidate(num, position_candidates):
    return all(symbol in position_candidates[i] for i, symbol in enumerate(num))


def meet_condition(candidate, nums):
    return len([num for num in nums if num == candidate]) > len(nums) / 3


class Solution2:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if not nums:
            return []
        symbols = string.digits + '+-'
        max_len = max(len(str(num)) for num in nums)
        nums = [normalize(num, max_len) for num in nums]
        position_candidates = (max_len + 1) * [[]]
        for i in range(max_len + 1):
            counter = 12*[0]
            for num in nums:
                counter[index(num[i])] += 1
            for pos in range(12):
                if counter[pos] > len(nums) / 3:
                    position_candidates[i].append(symbols[pos])
        candidates = [num for num in nums if is_candidate(num, position_candidates)]
        return sorted(int(candidate) for candidate in set(candidates) if meet_condition(candidate, nums))



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
    res = Solution2().majorityElement([1,1,1,1,1,1]) 
    print((2 + 1) * [[]])
    
    
    
    
    
    
    
    
    