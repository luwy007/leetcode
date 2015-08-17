'''  
@author: yang
'''
import numpy
class Fibonacci:
    def getNthNumber(self, n):
        
        # write code here
        if(n==1):
            return 1
        if(n==2):
            return 2
        mat = numpy.array([(1,1),(1,0)]) 
        binary = bin(n-2)[2:] 
        if(binary[-1]=='1'):
            transMat = mat#
        else:
            transMat = numpy.array([(1,0),(0,1)])
        
        for index in range(2,len(binary)+1): 
            mat = numpy.dot(mat,mat)
            if(binary[-index]=='1'):
                transMat = numpy.dot(transMat,mat)
        
        result = numpy.dot([1,2],transMat)
        return result[0]%1000000007
if __name__=="__main__":
    for i in range(5):
        result = Fibonacci().getNthNumber(i+1)   
        print(result)
        
        

