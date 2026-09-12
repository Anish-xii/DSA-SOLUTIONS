# in order triverse

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.count = k
        self.ans = 0
        
        def dfs(node):
            if not node: return
            
            dfs(node.left)
            if self.count == 1:
                self.ans = node.val
            self.count -= 1
            dfs(node.right)
        
        dfs(root)
        return self.ans