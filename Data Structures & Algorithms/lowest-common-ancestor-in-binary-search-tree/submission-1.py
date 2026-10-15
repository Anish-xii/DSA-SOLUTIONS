class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        curr_pos = root

        while curr_pos:
            # both nodes are smaller
            if p.val < curr_pos.val and q.val < curr_pos.val:
                curr_pos = curr_pos.left
            # both nodes are bigger
            elif p.val > curr_pos.val and q.val > curr_pos.val:
                curr_pos = curr_pos.right
            # node position splits
            else:
                return curr_pos