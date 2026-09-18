class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n: return True

        # 1. add all both directed nodes in graph (parent, child)
        pre_map = {i:[] for i in range(n)} # dict(list)
        
        for pn, cn in edges:
            pre_map[pn].append(cn)
            pre_map[cn].append(pn)

        
        # 2. for all conected nodes check "cycle"
        visited = set()
        stk = [(0, -1)]

        while stk:
            node, parent = stk.pop()
            if node in visited:
                return False
            visited.add(node)

            for neighbor in pre_map[node]:
                if neighbor != parent:
                    stk.append((neighbor, node))
        
        # 3. chek all node visited
        return len(visited) == n

        