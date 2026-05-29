# levels right-most eliment
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        que = collections.deque()
        que.append(root)
        res = []

        while que:       
            r_node = None     
            for i in range(len(que)):
                node = que.popleft()
                r_node = node
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)       
            
            res.append(r_node.val)

        return res 