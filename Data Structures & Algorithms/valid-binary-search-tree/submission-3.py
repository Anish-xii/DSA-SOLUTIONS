# going left gets prev as new maximum
# going right gets prev as new minimum

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        stk = [(float('-inf'), root, float('inf'))]
        
        while stk:
            low, node, hi = stk.pop()

            if not node: continue
            elif not (low < node.val < hi):
                return False
            
            if node.left: 
                stk.append((low, node.left, node.val))
            if node.right:
                stk.append((node.val, node.right, hi))
        
        return True   

# [6,2,8,0,9]
#.         -inf < 6 < inf
#.    -inf < 2 < (6) < 8 < inf
#-inf < 0 < (2)       (8) < 9 < inf
