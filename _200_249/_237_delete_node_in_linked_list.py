''' 
Created on 2015/7/23

@author: Administrator
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        while(node.next!=None):
            node.val = node.next.val
            if(node.next.next==None):
                del(node.next)
                node.next = None
                break
            node = node.next
        
    
     