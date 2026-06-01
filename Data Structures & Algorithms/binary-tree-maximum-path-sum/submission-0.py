class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = root.val

        def dfs(node):

            if not node: return 0

            maxleft = max(dfs(node.left), 0)
            maxright = max(dfs(node.right), 0)
            
            # 1. if path goes through cuu node
            self.res = max(self.res, node.val + maxleft + maxright)
            # 2. if path includes curr node
            return node.val + max(maxleft, maxright)

        dfs(root)    
        return self.res