# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
    	# if the tree is null, return 0
        if(not root):
            return 0
        firstFoundLeaf = True
        minDepth = 0
        depth = 0
        visited = []
        unvisited = []
        node = root
        while(node):
            depth += 1
            visited.append(node)
            # if-else judge based on whether the node is leaf
            # node is a leaf
            if(not node.left and not node.right): #the leaf node won't be pushed in the stack
                if(not firstFoundLeaf and depth<minDepth):
                    minDepth = depth
                if(firstFoundLeaf):
                    minDepth = depth
                    firstFoundLeaf = False
                # when the node is a leaf and unvisited is null, we have traversed the whole tree,return the maxDepth
                if(not unvisited):
                    return minDepth
                # roll back until find a proper node to visit 
                while(visited[-1].right!=unvisited[-1]):
                    visited.pop()
                    depth -= 1
                node = unvisited.pop()

            # node is not a leaf
            else:
                if(node.left and node.right):
                    unvisited.append(node.right) 
                    node = node.left 
                else: 
                    if(node.left):
                        node = node.left 
                    else:
                        node = node.right 


    def minDepthPath(self, root):
        path = []
        # if the tree is null, return 0
        if(not root):
            return 0

        firstFoundLeaf = True
        minDepth = 0
        depth = 0
        visited = []
        unvisited = []
        node = root
        while(node):
            depth += 1
            visited.append(node)
            path.append(node)
            # if-else judge based on whether the node is leaf
            # node is a leaf
            if(not node.left and not node.right): #the leaf node won't be pushed in the stack
                if(not firstFoundLeaf and depth<minDepth):
                    minDepth = depth
                    path = visited[:]
                if(firstFoundLeaf):
                    minDepth = depth
                    firstFoundLeaf = False
                    path = visited[:]
                # when the node is a leaf and unvisited is null, we have traversed the whole tree,return the maxDepth
                if(not unvisited):
                    return path
                # roll back until find a proper node to visit 
                while(visited[-1].right!=unvisited[-1]):
                    visited.pop()
                    depth -= 1
                node = unvisited.pop()

            # node is not a leaf
            else:
                if(node.left and node.right):
                    unvisited.append(node.right) 
                    node = node.left 
                else: 
                    if(node.left):
                        node = node.left 
                    else:
                        node = node.right

    			 









