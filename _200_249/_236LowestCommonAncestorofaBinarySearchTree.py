''' 
#-*- coding=utf-8 -*-
Created on 2015年7月23日  

@author: yang
'''
# Definition for a binary tree node.
from test.support import temp_cwd
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    
    def ref(self,root,p,q):
        stack = [[root, False]]
        pFind = False
        qFind = False
        ancestor = None
    
        while stack:
            curr, visited = stack.pop()
            if curr is not None:
                if visited:
                    # update temporary ancestor
                    if curr.left is ancestor or curr.right is ancestor:
                        ancestor = curr
                    # p and q occupy each side of tree respectively
                    if curr is root and (qFind or pFind):
                        return root
                else:
                    # Find both nodes
                    if (pFind and curr is q) or (qFind and curr is p):
                        return ancestor
    
                    if curr is p:
                        pFind = True
                        ancestor = p
                    elif curr is q:
                        qFind = True
                        ancestor = q
    
                    stack.append([curr, True])
                    stack.append([curr.right, False])
                    stack.append([curr, True])
                    stack.append([curr.left, False])
    
    def lowestCommonAncestor(self, root, p, q): 
        path1 = []
        path2 = [] 
        
        node = root
        self.depthFirst(node, path1, p)
                
        node = root
        self.depthFirst(node, path2, q)
            
        LCA = root
        length = 0
        if(len(path1)<len(path2)):
            length = len(path1)
        else:
            length = len(path2)
        for index in range(length):
            if(path1[index]==path2[index]):
                LCA=path1[index]
            else:
                break
            
        return LCA
        
    def depthFirst(self,node,path,p):
        if(node!=None):
            path.append(node)
            if(node==p):
                return True
            else:
                if(self.depthFirst(node.left, path, p)):
                    return True
                elif(self.depthFirst(node.right, path, p)):
                    return True
                else:
                    path = path.pop()
                    return False
        else:
            return False
    
    def buildTree(self,l):
        root = TreeNode(l[0])
        path = [root]
        index = 0
        left = True
        for index,item in l[1:]:
            if(item!=None):
                temp = TreeNode(item)
            else:
                temp = None
            if(left):
                if(path[index]!=None):
                    path[index].left = temp
                path.append(temp)
            else:
                left = False
                if(path[index]!=None):    
                    path[index].right = temp
                index += 1
                path.append(temp)
    
    
                    
l = [1,2,3]              
def func(l):
    l = l.pop()  
        
if __name__=="__main__":
    func(l)
    print(l)

















                