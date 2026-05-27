class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        if not root.left and not root.right: return 1

        stk = [[root, 1]]
        dth = 0

        while stk:
            node, d = stk.pop()

            if node.left: 
                dth = max(dth, d+1)
                stk.append([node.left, d+1])
            if node.right: 
                dth = max(dth, d+1)
                stk.append([node.right, d+1])

        return dth        
