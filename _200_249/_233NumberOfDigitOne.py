''' 
Created on 2015/8/2 

@author: yang
'''
class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        if(n<1):
            return 0
        length = 0
        temp = n
        while(temp>=1):
            temp//=10
            length += 1
        
        
        count = 0
        for i in range(length-1): #from second digit to the last one
            head = n//(10**(i+1))
            tail = n%(10**i)
            mid = n//(10**i)%10
            if(mid<1):
                head -= 1
                tail = 10**i-1
            elif(mid>1):  
                tail = 10**i-1
            count += head*10**i+tail+1
        
        if(n//(10**(length-1))==1):
            count += n%(10**(length-1))+1
        else:
            count += 10**(length-1)   
        
        return count


if __name__=="__main__":
    obj = Solution()
    print(obj.countDigitOne(8192))