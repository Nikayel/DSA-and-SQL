class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Have a PreReqs Map
        preMap = {i : [] for i in range(numCourses)}
        #visiting set
        for course,Pres in prerequisites:
            preMap[course].append(Pres)  

        visiting = set()
        #DFS function(course)
        def dfs(crs):

            #base case:
                #if visited -> return False
            if crs in visiting:
                return False
                
            visiting.add(crs)
            for pres in preMap[crs]:
                if not dfs(pres):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
