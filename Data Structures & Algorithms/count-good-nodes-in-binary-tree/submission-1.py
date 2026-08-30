# for all node dfs is the node bigger than the max we allredy seen
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stk = [(root, root.val)]
        count = 0

        while stk:
            node, max_val = stk.pop()
            if node.val >= max_val:
                count += 1
            
            new_max = max(node.val, max_val)

            if node.left:
                stk.append((node.left, new_max))
            if node.right:
                stk.append((node.right, new_max))
        
        return count