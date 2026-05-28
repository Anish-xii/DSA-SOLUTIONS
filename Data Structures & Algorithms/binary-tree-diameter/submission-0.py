# for all node -> their l_height + r_height
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = [0]

        def dfs(root):
            if not root: return 0

            lft = dfs(root.left)
            rte = dfs(root.right)
            res[0] = max(res[0], lft + rte)
            return 1 + max(lft, rte)

        dfs(root)
        return res[0] 