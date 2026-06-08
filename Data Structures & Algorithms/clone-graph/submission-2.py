#self.val = val
#self.neighbors -> a list

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        stk = [node]
        old_n = {node: Node(node.val)}

        while stk:
            n = stk.pop()
            for nbr in n.neighbors:

                if nbr not in old_n:
                    stk.append(nbr)
                    old_n[nbr] = Node(nbr.val)

                old_n[n].neighbors.append(old_n[nbr])        

        return old_n[node]  