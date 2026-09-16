from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node: return None
        
        old_new = {}

        def dfs(n):
            if n in old_new: 
                return old_new[n]
            
            new_n = Node(val = n.val)
            old_new[n] = new_n

            # List<Node> neighbors;
            new_n.neighbors = [dfs(nbr) for nbr in n.neighbors] 

            return new_n
        

        return dfs(node)