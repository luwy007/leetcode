'''  

@author: yang
'''
class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        chars = []
        for char in s:
            if((char<='9' and char>='0') or char=='+' or char=='-' or char=='*' or char=='/'):
                chars.append(char)
        nums = [] 
        operators = []
        num = 0
        for item in chars:
            if(item<='9' and item>='0'):
                num*=10
                num += int(item)
            elif(item=='+' or item=='-' or item=='*' or item=='/'):
                nums.append(num)
                num = 0
                operators.append(item) 
        nums.append(num)
        if not operators:
            return num
        
        nums2 = [nums[0]]
        operators2 = ['+']
        for index,num in enumerate(nums[1:]):
            if(operators[index]=="*"): 
                temp = nums2.pop()
                temp *= num
                nums2.append(temp)
            elif(operators[index]=='/'):
                temp = nums2.pop()
                temp //= num
                nums2.append(temp)
            else:
                operators2.append(operators[index])
                nums2.append(num)
        
        result = 0
        for index, operator in enumerate(operators2):
            if(operator=="+"):
                result += nums2[index]
            else:
                result -= nums2[index]
                
        return result 
    
print(Solution().calculate("2*3+4/5"))























