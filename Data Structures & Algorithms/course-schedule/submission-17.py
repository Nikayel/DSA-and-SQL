class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #get the prereq for each item 
        prereqs = {i: [] for i in range(numCourses)}
        for pre, crs in prerequisites:
            prereqs[crs].append(pre)
        #recusrvisely go through each pre reqs $ empty pre reqs True immedietly $ empty the prereqs
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if prereqs[crs] == []:
                return True
            visiting.add(crs)
            for pre in prereqs[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            prereqs[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



            