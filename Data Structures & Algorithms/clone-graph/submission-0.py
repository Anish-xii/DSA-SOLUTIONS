#self.val = val
#self.neighbors -> a list

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        old_new = {}

        def dfs(node):
            if node in old_new: return old_new[node]
            n_node = Node(node.val)
            old_new[node] = n_node
            
            # nbr of node in list neighbors
            for nbr in node.neighbors:
                n_node.neighbors.append(dfs(nbr))
            
            return n_node    

        return dfs(node) if node else None