#self.val = val
#self.neighbors -> a list

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        srt = node
        stk = [srt]
        old_n = {srt: Node(srt.val)}

        while stk:
            n = stk.pop()
            for nbr in n.neighbors:
                if nbr not in old_n:
                    stk.append(nbr)
                    old_n[nbr] = Node(nbr.val)
        
        for o, n in old_n.items():
            for nbr in o.neighbors:
                n.neighbors.append(old_n[nbr])     

        return old_n[srt] 