# if the node is present in the same pos
# if that node has the same vale

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        stk = [(p, q)]


        while stk:
            node1, node2 = stk.pop()

            if not node1 and not node2: 
                continue
            elif node1 and node2 and node1.val == node2.val:
                stk.append((node1.left, node2.left))
                stk.append((node1.right, node2.right))
            else:
                return False
        
        return True