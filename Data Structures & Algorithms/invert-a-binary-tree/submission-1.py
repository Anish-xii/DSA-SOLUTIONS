# stk
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root: return None
        que = deque([root])

        while que:
            node = que.popleft()
            node.left, node.right = node.right, node.left
            if node.left: que.append(node.left)
            if node.right: que.append(node.right)

        return root 