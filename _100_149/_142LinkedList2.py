'''  

@author: yang
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None 

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        node = self.hasCycle(head)
        if(node==None):
            return node
        else:
            cycle = 1
            temp = node
            while(temp.next!=node):
                temp = temp.next
                cycle += 1  
                
            length = 0
            temp = head
            while(temp!=node):
                temp = temp.next
                length += 1 
            temp = head
            for i in range((length//cycle-1)*cycle):
                temp = temp.next 
            
            while(temp!=node):
                temp,node = temp.next,node.next
            
            return node
    
            
            
    
    def hasCycle(self, head):
        if(head==None):
            return None
        node1 = head
        node2 = head
        while(node1.next!=None and node2.next!=None):
            node1 = node1.next
            node2 = node2.next
            if(node2.next!=None):
                node2 = node2.next 
            else:
                return None
            if(node1==node2):
                return node1 
        return None


if __name__=="__main__":
    for i in range(4):
        print("uyes")  
    
    
    
    