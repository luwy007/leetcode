'''  
@author: yang
'''
class Solution: 
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):  
        if(len(s)<=1):
            return s
        next = self.buildNext(s)
        j = 1
        i = 0
        preindex = 0 
        while(i+j<len(s)):
            while(s[-j]==s[i] and i+j<len(s)):
                i += 1
                j += 1
            
            if(s[i]==s[-j]):
                if(i+j==len(s)):
                    preindex = 2*i+1
                else:
                    preindex = 2*(i+1)
            
            else:
                while(s[-j]!=s[i] and next[i]!=-1):
                    i = next[i]
                if(s[-j]==s[i]):
                    continue
                else:
                    i = 0
                    j += 1
                    
        if((i+j)==len(s)-1):
            preindex = 2*(i+1)  #preindex represents s[:preindex] is parlindrome
                
        elif(i+j>len(s)):
            preindex = 2*i
        
        else:
            preindex = 2*i+1
        
        
        result = ""
        for index in range(preindex,len(s)):
            result += s[-(index-preindex+1)]
        result += s
        
        return result
    
    def isParlindrome(self,s):
        length = len(s)//2 
        temp = s[-length:]
        temp.reverse()
        if (s[:length]==temp):
            return True
        return False
    
    def buildNext(self,pattern):
        #=======================================================================
        # next[j]=k means P0P1..Pk==Pj-k Pj-k+1 Pj-1
        # next[0] could be initialized as 0
        #================================== =====================================
        NEXT = [-1,0]
        if(len(pattern)==2):
            return NEXT
        k = 0  
        for j in range(2,len(pattern)): 
            if(pattern[j-1]==pattern[k]):
                NEXT.append(NEXT[-1]+1)
                k += 1 
            else:
                while(pattern[j-1]!=pattern[k]):# item means pattern[j]
                    k=NEXT[k] 
                    if(k==-1): 
                        break
                if(k==-1):
                    NEXT.append(0)
                    k = 0
                elif(pattern[k]==pattern[j-1]): 
                    NEXT.append(k+1)
                    k += 1
        
        #advanced next edition
        for tu in enumerate(NEXT):
            index = tu[0]
            if(NEXT[index]==-1):
                continue
            while(pattern[index]==pattern[NEXT[index]]):
                NEXT[index] = NEXT[NEXT[index]]
                if(NEXT[index]==-1):
                    break
            
        
        return NEXT


if __name__=="__main__": 
    s = "2"
    result = Solution().shortestPalindrome(s)
    print(result)
    
    
    
    
    
    