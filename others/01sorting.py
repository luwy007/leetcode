'''  
@author: yang
'''
class Solution:
    def __init__(self):
        pass
    
    def counting(self,s):
        i = 0
        j = 1
        count = 0
        while(i+j<len(s)):
            while(i+j<len(s) and s[i]!="1"):
                i += 1
            while(i+j<len(s) and s[-j]!="0"):
                j += 1
            
            if(i+j<len(s)):
                if(s[i]=='1' and s[-j]=='0'):
                    i += 1
                    j += 1
                    count += 1
                else:
                    return count
        
        return count
                
    
if __name__=="__main__":
    strs = ["01","10","110","1100","01000001111100"]
    for s in strs:
        res = Solution().counting(s)   
        print(s,res) 
    
    f = input("first: ")
    s = input("second: ")
    print(f)
    
    
    
    