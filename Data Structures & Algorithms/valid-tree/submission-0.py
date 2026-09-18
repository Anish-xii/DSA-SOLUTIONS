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

        def dfs(i, parent):
            visited.add(i)

            for child in pre_map[i]:
                # if pointing back to parent (no problem)
                if child == parent: continue
                if child in visited:
                    return False
                if not dfs(child, i):
                    return False
            
            return True
        
        # 3. check all node present
        return dfs(0, -1) and len(visited) == n

        