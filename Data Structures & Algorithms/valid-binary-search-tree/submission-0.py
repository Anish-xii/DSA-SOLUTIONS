# see the tree upside down [-inf/n.prev < n < inf/n.prev]
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, mn, mx):
            if not node: return True
            if not (mn < node.val < mx): return False
            return dfs(node.left, mn, node.val) and dfs(node.right, node.val, mx)

        return dfs(root, float('-inf'), float('inf'))    