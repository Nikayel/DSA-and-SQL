class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #Create a map of prereqs
        preReqs = {i: [] for i in range(numCourses)}
        #do DFS on it and detect a cycle
        for crs,pre in prerequisites:
            preReqs[crs].append(pre)
        visited = set()
        def dfs(courses):
            #if cycle return False
            if courses in visited:
                return False
                #recursively call this on its prereqs too
            visited.add(courses)
            for nei in preReqs[courses]:
                    #Clear the current Course and pres
                if not dfs(nei):
                    return False
            visited.remove(courses)
            preReqs[courses] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        #calls dfs - if False return False else True
        return True