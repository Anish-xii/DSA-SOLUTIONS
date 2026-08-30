# O(M * N) recursion DFS
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # check same tree function
        def same(a, b):
            if not a and not b: 
                return True
            if a and b and a.val == b.val: 
                return same(a.left, b.left) and same(a.right, b.right)
            return False
        
        # run same-tree for all nodes in tree
        def dfs(node):
            if not node:
                return False
            if same(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)