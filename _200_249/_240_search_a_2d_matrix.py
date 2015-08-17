'''
Created on 2015-7-23

@author: Administrator
'''

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            
            head = 0
            tail = len(matrix[i])-1
            while(head<tail-1):
                if(matrix[i][(head+tail)//2]>target):
                    tail = (head+tail)//2
                else:
                    head = (head+tail)//2
            if(matrix[i][head]==target or matrix[i][tail]==target):
                return True 
        return False
                
    def binary_search(self, l, target):
         
        head = 0
        tail = len(l)-1
        while(head<tail-1):
            if(l[(head+tail)//2]>target):
                tail = (head+tail)//2+1
            else:
                head = (head+tail)//2
        if(l[head]==target or l[tail]==target):
            return True
        else:
            return False
         
if __name__=="__main__":
    l = [1,2,3,4] 
    print(l[-1])

        
        