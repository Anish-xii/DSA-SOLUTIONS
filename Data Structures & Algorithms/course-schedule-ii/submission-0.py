class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        # 1. map all courses to its prereq-courses 
        pre_map = defaultdict(list)
        
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        order = []
        visiting = set()
        visited = set()


        def dfs(crs):
            if crs in visiting: return False
            if crs in visited: return True

            visiting.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre): return False
            
            visited.add(crs)
            visiting.remove(crs)
            order.append(crs)
            return True
        

        # 2. for all crses chek if they end or not
        for crs in range(numCourses):
            if not dfs(crs): return []
        
        return order