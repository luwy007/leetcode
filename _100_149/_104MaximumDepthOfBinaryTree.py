# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
    	# if the tree is null, return 0
    	if(not root):
    		return 0

    	maxDepth = 0
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
    			if(depth>maxDepth):
    				maxDepth = depth
    			# when the node is a leaf and unvisited is null, we have traversed the whole tree,return the maxDepth
    			if(not unvisited):
    				return maxDepth
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
    #return the path from root to the farest leaf node
    def maxDepthPath(self, root):
        # if the tree is null, return 0
        if(not root):
            return 0

        maxDepth = 0
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
                if(depth>maxDepth):
                    maxDepth = depth
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


    			 









