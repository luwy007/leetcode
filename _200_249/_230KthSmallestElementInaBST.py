'''  
@author: yang
'''
# Definition for a binary tree node.
from lib2to3.pytree import Node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k): 
        stack = []
        count = 0
        node = root
        stack.append(node)
        while True:
            while(node.left is not None): #keep the pop of stack is the most count-th smallest in the BST
                stack.append(node.left)
                node = node.left
                
            node = stack.pop()
            count += 1    
            while(node.right is None and count<k and stack):
                node = stack.pop()
                count += 1
                
            if(count==k):
                return node.val
                    
                
            if(node.right is not None and count<k):
                stack.append(node.right)
                node = node.right
                
                
            
                
                
                
if __name__=="__main__":
    root = TreeNode(2)
    node = TreeNode(1)
    root.left = node 
    node = TreeNode(3)
    root.right = node  
    print(Solution().kthSmallest(root, 3))
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                