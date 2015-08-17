'''  

@author: yang
'''
class Queue:
    
    # initialize your data structure here.
    def __init__(self): 
        self.stack = []
        self.size = 0
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        self.size += 1

    # @return nothing
    def pop(self): 
        temp = []
        size = self.size
        while(size>1):
            top = self.stack.pop()
            temp.append(top)
            size -= 1
        result = self.stack.pop()
        while temp:
            top = temp.pop()
            self.stack.append(top)
        self.size -= 1
    # @return an integer
    def peek(self): 
        if(self.size<1):
            return False
        temp = []
        size = self.size
        while(size>1):
            top = self.stack.pop()
            temp.append(top)
            size -= 1
        result = self.stack.pop()
        self.stack.append(result)
        while temp:
            top = temp.pop()
            self.stack.append(top)
        return result
    # @return an boolean
    def empty(self):
        return self.size==0
        
        
if __name__=="__main__":
    obj = Queue()
    obj.push(1)
    obj.push(2) 
    obj.pop()
    temp = obj.peek()  
    print(temp)     
        