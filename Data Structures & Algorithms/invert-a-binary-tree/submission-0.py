# stk
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root: return None
        stk = [root]

        while stk:
            node = stk.pop()
            node.left, node.right = node.right, node.left
            if node.left: stk.append(node.left)
            if node.right: stk.append(node.right)

        return root 