# for every node -> check height diffrence of l and r < 1
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        res = [True]

        def dfs(node):
            if not node: return 0

            l_hgt = dfs(node.left)
            r_hgt = dfs(node.right)

            if abs(l_hgt - r_hgt) > 1: 
                res[0] = False
                return -1

            return 1 + max(l_hgt, r_hgt)

        dfs(root)
        return res[0] 