
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        que = collections.deque()
        que.append(root)
        res = []

        while que:
            level = []
            
            for i in range(len(que)):
                node = que.popleft()
                level.append(node.val)
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)       
            
            res.append(level)

        return res                             