class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapPres = {i: [] for i in range(numCourses)}
        #Loop current over preRerqs
        for crs,preReqs in prerequisites:
            mapPres[crs].append(preReqs)
            #Map[current].append()

        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            
            visiting.add(course)
            for pres in mapPres[course]:
                if not dfs(pres):
                    return False
            visiting.remove(course)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True