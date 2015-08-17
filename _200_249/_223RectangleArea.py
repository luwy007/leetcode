'''  
@author: yang
'''
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H): 
        if(G<A or C<E or B>H or D<F):
            return (C-A)*(D-B)+(G-E)*(H-F)
        length = 0
        width = 0
        
        if(A<=E and C<=G):
            length = C-E
        elif(E<=A and C<=G):
            length = C-A
        elif(A<=E and G<=C):
            length = G-E
        elif(E<=A and G<=C):
            length = G-A
            
        
        if(B<=F and D<=H):
            width = D-F
        elif(F<=B and D<=H):
            width = D-B
        elif(B<=F and H<=D):
            width = H-F
        elif(F<=B and H<=D):
            width = H-B
            
        return (C-A)*(D-B)+(G-E)*(H-F)-length*width   



result = Solution().computeArea(-2,-2,2,2,-2,-2,2,2)

print(result)













