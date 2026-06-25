class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pres = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            pres[crs].append(pre)
        
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if pres[crs] == []:
                return True
            visiting.add(crs)
            for pre in pres[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            pres[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
          