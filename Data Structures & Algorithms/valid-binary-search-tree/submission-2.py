# going left gets prev as new maximum
# going right gets prev as new minimum

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, miin, maax):
            if not node: 
                return True
            if not (miin < node.val < maax):
                return False
            
            return dfs(node.left, miin, node.val) and dfs(node.right, node.val, maax)

        
        return dfs(root, float('-inf'), float('inf'))    

# [6,2,8,0,9]
#.         -inf < 6 < inf
#.    -inf < 2 < (6) < 8 < inf
#-inf < 0 < (2)       (8) < 9 < inf
