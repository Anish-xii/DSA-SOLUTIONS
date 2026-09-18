class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # 1. add all both directed nodes in graph (parent, child)
        pre_map = {i:[] for i in range(n)} # dict(list)
        
        for pn, cn in edges:
            pre_map[pn].append(cn)
            pre_map[cn].append(pn)
        

        # 2. cross/visit all nonnections
        def dfs(node):
            for cld in pre_map[node]:
                if cld not in visited:
                    visited.add(cld)
                    dfs(cld)
        

        # 3. for all nodes check connections
        visited = set()
        res = 0

        for node in range(n):
            # if alredy visited skip
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1
        
        return res

        