# using stack 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        pos = 0
        stk = []
        curr = root

        while curr or stk:
            
            while curr: 
                stk.append(curr)
                curr = curr.left 
            
            curr = stk.pop()
            pos += 1
            if pos == k: return curr.val
            curr = curr.right 