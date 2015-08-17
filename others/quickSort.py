'''  
@author: yang
'''
from tkinter.constants import ANCHOR
class Solution: 
    def __init__(self):
        pass
    
    def quickSort(self,nums,h,t):#sorting nums[h:t+1]
        if(h>=t):
            return
        else:
            i = h+1
            j = t
            
            while(i<j):
                while(i<j and nums[i]<nums[h]):
                    i += 1
                while(i<j and nums[j]>=nums[h]):
                    j -= 1
                    
                nums[i],nums[j] = nums[j],nums[i]  #after reversing, nums[i]<nums[h], nums[j]>=nums[h]
                i+=1
                j-=1
                
            if(i==j):
                if(nums[h]>nums[i]):
                    nums[h],nums[i] = nums[i],nums[h]
                    self.quickSort(nums, h, i-1)
                    self.quickSort(nums, i+1, t)
                else:
                    nums[h],nums[i-1] = nums[i-1],nums[h]
                    self.quickSort(nums, h, i-2)
                    self.quickSort(nums, i, t)
            else:
                nums[h],nums[j] = nums[j],nums[h]
                self.quickSort(nums, h, j-1)
                self.quickSort(nums, j+1, t)
             
    
if __name__=="__main__":
    nums = [6,5,3,1,2,6,8,7,9]
    Solution().quickSort(nums, 0, len(nums)-1)       
    print(nums)
    
    
    
    
    
    
    
    
    
    
    
    
    