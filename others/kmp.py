'''  
@author: yang
'''
class KMP:
    #@para string pattern
    #@para string s is the string matched
    def PatternMatch(self,pattern,s):
        NEXT = self.buildNext(pattern)
        j = 0
        for i in range(len(s)):
            if(s[i]==pattern[j]):
                j += 1
                if(j==len(pattern)):
                    return i-len(pattern)+1 
            else:
                while(pattern[j]!=s[i]):
                    j=NEXT[j]
                    if(j==-1):
                        j = 0
                        break
                
    
    
    
    
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
    s = "abcabceabcde"
    pattern = "abaabcaba" 
    index = KMP().PatternMatch(pattern, s)
    print(index)