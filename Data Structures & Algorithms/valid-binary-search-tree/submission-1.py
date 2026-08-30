# see the tree upside down [-inf/n.prev < n < inf/n.prev]
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, miin, maax):
            if not node: 
                return True
            if not (miin < node.val < maax):
                return False
            
            return dfs(node.left, miin, node.val) and dfs(node.right, node.val, maax)

        
        return dfs(root, float('-inf'), float('inf'))    