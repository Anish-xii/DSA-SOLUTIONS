# for all node dfs is the node bigger than the max we allredy seen
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxnum):
            if not node: return 0

            res = 1 if node.val >= maxnum else 0
            maxnum = max(maxnum, node.val)
            res += dfs(node.left, maxnum)
            res += dfs(node.right, maxnum)
            return res

        return dfs(root, root.val)