class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        # 1. map all courses to its prereq-courses 
        pre_map = {i:[] for i in range(numCourses)} # or defaultdict()
        
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)


        visiting = set()

        def dfs(crs):
            if crs in visiting: return False
            if pre_map[crs] == []:
                return True
            # else we have prereq to check
            visiting.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre): return False
            # when all node has an ending
            pre_map[crs] = []
            visiting.remove(crs)
            return True
        

        # 2. for all crses chek if they end or not
        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True


     