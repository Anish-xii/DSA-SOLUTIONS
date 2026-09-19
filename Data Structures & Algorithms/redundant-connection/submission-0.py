class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:

        n = len(edges)
        parent = list(range(n+1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]


        for u, v in edges:
            u_root, v_root = find(u), find(v)
            if u_root == v_root:
                return [u, v]
            parent[u_root] = v_root
        
        return []