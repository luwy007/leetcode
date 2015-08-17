'''  

@author: yang
'''
# Definition for singly-linked list.
from pip._vendor.distlib._backport.tarfile import TUREAD
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if(head==None):
            return False
        node1 = head
        node2 = head
        while(node1.next!=None and node2.next!=None):
            node1 = node1.next
            node2 = node2.next
            if(node2.next!=None):
                node2 = node2.next 
            else:
                return False
            if(node1==node2):
                return True 
        return False
        